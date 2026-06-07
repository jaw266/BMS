from flask import Flask, request, redirect, url_for , render_template, render_template_string, make_response
from database import MeasurementDB
from config import DATABASE_URL
import dashboard_html, history_html
from datetime import datetime
from config import *

app = Flask(__name__)
app.config.from_object('config')

database = MeasurementDB(DATABASE_URL)

@app.route('/insertMesures', methods=['GET'])
def insertMesures():
	voltage1	= request.args.get('voltage1')
	voltage2	= request.args.get('voltage2')
	voltage3	= request.args.get('voltage3')
	current		= request.args.get('current')
	temperature	= request.args.get('temperature')
	soc			= request.args.get('soc')
	soh			= request.args.get('soh')

	if None in (voltage1, voltage2, voltage3,current, temperature, soc, soh):
		return 'il y a un parametres qui manque'

	if not database.insert_measurement(voltage1, voltage2, voltage3, current, temperature, soc, soh):
		return 'impossible dinserer danas la base des données'

	return 'OK'

@app.route('/', methods=['GET'])
def home():
	mesure = database.get_last_measurements(1)

	if len(mesure):
		print(mesure[0])
		v1	=  mesure[0].voltage1
		v2	=  mesure[0].voltage2
		v3	=  mesure[0].voltage3
		i	=  mesure[0].current
		soc =  mesure[0].soc
		t	=  mesure[0].temperature
		soh	=  mesure[0].soh
		return render_template_string(dashboard_html.monitor(v1, v2, v3, i, soc, t, soh))
	else:
		return render_template_string(dashboard_html.monitor(0,0,0,0,0,0,0))


@app.route('/history', methods=['GET'])
def history():
	date_from = request.args.get('DateDebut')
	date_to = request.args.get('DateFin')

	try:
		date1 = datetime.strptime(str(date_from), '%Y-%m-%dT%H:%M').timestamp()
	except:
		date1 = None

	try:
		date2 = datetime.strptime(str(date_to), '%Y-%m-%dT%H:%M').timestamp()
	except:
		date2 = None

	print(date1, date2)
	if date1 == date2 == None:
		mesures = database.get_all_measurements()
		return render_template_string(history_html.history(mesures))
	elif date1 is not None:
		if date2 is None:
			mesures = database.get_measurements_between_dates(date1)
		else:
			mesures = database.get_measurements_between_dates(date1, date2)
		return render_template_string(history_html.history(mesures))
	else:
		return render_template_string(history_html.history([]))



####################### MAIN LOOP ################
if __name__ == '__main__':
	app.run(debug=app.config["DEBUG"], port=PORT, host=HOST)

