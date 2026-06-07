import serial
import RPI.GPIO as GPIO
import requests
import time

url = 'http://192.168.9.24:3000/insertMesures' 
device = '/dev/ttyACM0'

#UART Communication avec la carte arduino
rx_pin = 15  
GPIO.setmode(GPIO.BCM)
GPIO.setup(rx_pin, GPIO.IN)  
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)  

while True:
	if GPIO.input(rx_pin):
		#lecture des donnes a partir de la carte arduino 
		data = ser.readline().decode().strip()
		split_values = data.split('/')
		if len(split_values) >= 6:
			voltage1 = split_values[0]
			voltage2 = split_values[1]
			voltage3 = split_values[2]
			Temp = split_values[3]
			Current = split_values[4]
			Soh=split_values[5]
			SOH=float(Soh)-10.00
			Soh=str(SOH)
			Soc=format(100*(float(voltage1)+float(voltage2)+float(voltage3))/12.6,'.2f')

	params = {
    	'voltage1': voltage1,
    	'voltage2': voltage2,
		'voltage3': voltage3,
    	'current': Current,
    	'temperature': Temp,
    	'soc': Soc,
    	'soh': Soh,
	}
	try:
		response = requests.get(url, params=params)
		response.raise_for_status()  
		print("Request sent successfully!")
	except requests.exceptions.RequestException as e:
		print(f"An error occurred: {e}")
		
	time.sleep(60)