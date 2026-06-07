from config import *
from datetime import datetime

def setVoltageColor(volt):
	if volt <= VoltageLevel["BLUE"]:
		return "cyan"
	elif volt >= VoltageLevel["RED"]:
		return "red"
	else:
		return "green"

def setVoltageTotColor(volt):
	if volt <= VoltageTotLevel["BLUE"]:
		return "cyan"
	elif volt >= VoltageTotLevel["RED"]:
		return "red"
	else:
		return "green"

def setCurrentColor(current):
	if current <= CurrentLevel["BLUE"]:
		return "cyan"
	elif current >= CurrentLevel["RED"]:
		return "red"
	else:
		return "green"


def setTemperatureColor(temp):
	if temp <= TemperatureLevel["BLUE"]:
		return "cyan"
	elif temp >= TemperatureLevel["RED"]:
		return "red"
	else:
		return "green"


def setBatteryColor(charge):
	if charge <= BatteryLevel["RED"]:
		return "red"
	elif charge > BatteryLevel["RED"] and charge < BatteryLevel["ORANGE"]:
		return "red"
	elif charge >= BatteryLevel["ORANGE"] and charge < BatteryLevel["YELLOW"]:
		return "orange"
	elif charge >= BatteryLevel["YELLOW"] and charge < BatteryLevel["GREEN"]:
		return "yellow"
	else:
		return "green"


def setBatteryLevelImg(charge):
	if charge <= BatteryLevel["RED"]:
		return "static/img/battery_level_1.png"
	elif charge > BatteryLevel["RED"] and charge < BatteryLevel["ORANGE"]:
		return "static/img/battery_level_1.png"
	elif charge >= BatteryLevel["ORANGE"] and charge < BatteryLevel["YELLOW"]:
		return "static/img/battery_level_2.png"
	elif charge >= BatteryLevel["YELLOW"] and charge < BatteryLevel["GREEN"]:
		return "static/img/battery_level_3.png"
	else:
		return "static/img/battery_level_4.png"


def parseHistoryTable(mesures):
	ret = ''
	for mesure in mesures:
		ret += f'''<tr style="font-size:22px; white-space: nowrap;" >
			<td style="background-color: {setVoltageColor(mesure.voltage1)} ;"> {mesure.voltage1:.2f}</td >
			<td style="background-color: {setVoltageColor(mesure.voltage2)} ;"> {mesure.voltage2:.2f} </td >
			<td style="background-color: {setVoltageColor(mesure.voltage3)} ;"> {mesure.voltage3:.2f} </td >
			<td style="background-color: {setVoltageTotColor(mesure.voltage1+mesure.voltage2+mesure.voltage3)} ;">{mesure.voltage1 + mesure.voltage2 + mesure.voltage3:.2f}</td >
			<td style="background-color: {setCurrentColor(mesure.current)};">{mesure.current:.2f}</td >
			<td style="background-color: {setTemperatureColor(mesure.temperature)};">{mesure.temperature:.2f}</td >
			<td style="background-color: {setBatteryColor(mesure.soc)};">{mesure.soc:.2f}</td >
			<td style="background-color: {setBatteryColor(mesure.soh)};">{mesure.soh:.2f}</td >
			<td> {datetime.fromtimestamp(mesure.timestamp).strftime('%Y-%m-%d %H:%M:%S')}</td >
		</tr>'''
	return ret
