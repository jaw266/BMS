from sqlalchemy import create_engine, Column, Integer, Float, DateTime, desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time

Base = declarative_base()

class Measurement(Base):
	__tablename__ = 'mesure'

	id			= Column(Integer, primary_key=True)
	voltage1	= Column(Float)
	voltage2	= Column(Float)
	voltage3	= Column(Float)
	current		= Column(Float)
	temperature	= Column(Float)
	soc			= Column(Float)
	soh			= Column(Float)
	timestamp	= Column(Float)

class MeasurementDB:
	def __init__(self, db_uri):
		self.engine = create_engine(db_uri)
		Base.metadata.create_all(self.engine)
		self.Session = sessionmaker(bind=self.engine)

	def insert_measurement(self, voltage1, voltage2, voltage3, current, temperature, soc, soh):
		session = self.Session()
		isOK = False
		try:
			measurement = Measurement(
				voltage1	= voltage1,
				voltage2	= voltage2,
				voltage3	= voltage3,
				current		= current,
				temperature	= temperature,
				soc			= soc,
				soh			= soh,
				timestamp=time.time()
			)
			session.add(measurement)
			session.commit()
			isOK = True
		except SQLAlchemyError as e:
			session.rollback()
			print('erreur dans linsertion des mesures :', e)
		finally:
			session.close()
		return isOK

	def get_all_measurements(self):
		session = self.Session()
		try:
			measurements = session.query(Measurement).order_by(desc(Measurement.timestamp)).all()

		except SQLAlchemyError as e:
			print('erreur dans la mesure de:', e)
			measurements = []
		finally:
			session.close()
			return measurements

	def get_measurements_between_dates(self, start_date, end_date = time.time()):
		session = self.Session()
		try:
			measurements = session.query(Measurement).filter(Measurement.timestamp.between(start_date, end_date)).order_by(desc(Measurement.timestamp)).all()
		except SQLAlchemyError as e:
			print('Erreur dans la mesure entre les dates:', e)
			measurements = []
		finally:
			session.close()
			return measurements

	def get_last_measurements(self, num_measurements):
		session = self.Session()
		try:
			measurements = session.query(Measurement).order_by(Measurement.timestamp.desc()).limit(num_measurements).all()
		except SQLAlchemyError as e:
			print('erreur dans la prise des derniers mesures:', e)
			measurements = []
		finally:
			session.close()
			return measurements



