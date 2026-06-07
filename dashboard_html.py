from htmlParser import setVoltageColor, setCurrentColor, setTemperatureColor, setBatteryColor, setBatteryLevelImg

from flask import request
from urllib.parse import urlparse

def monitor(v1, v2, v3, i, soc, t, soh):
	URL			= request.url
	URL_BASE	= f"{urlparse(URL).scheme}://{urlparse(URL).netloc}"	# get basic URL example http://192.168.1.10:5000/

	ONCLICK_DASHBOARD	= f'''onclick="window.location.href='{URL_BASE}/';"'''
	ONCLICK_HISTORY		= f'''onclick="window.location.href='{URL_BASE}/history';"'''

	return "<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset=\"UTF-8\" http-equiv=\"refresh\" content=\"10\">\n\t<title>Battery Dashboard</title>\n\t<link rel=\"stylesheet\" href=\"static/style.css\">\n</head>\n<body>\n\t<nav>\n\t\t<div class=\"navbar-left\">\n\t\t  <button class=\"btn-dashboard\" {}>Dashboard</button>\n\t\t</div>\n\t\t<div class=\"navbar-right\">\n\t\t  <button class=\"btn-history\" {}>History</button>\n\t\t</div>\n\t</nav>\n\t<div class=\"container\">\n\t\t<div class=\"item\" style=\"grid-row: 1 / 2; grid-column: 1 / 2;\">\n\t\t\t<h2>Voltage 1</h2>\n\t\t\t<img src=\"static/img/volt.png\" alt=\"Battery\">\n\t\t\t<div class=\"progressbar\">\n\t\t\t\t<progress max=\"100\" value=\"50\" style=\"accent-color: {};\"></progress>\n\t\t\t</div>\n\t\t\t<p style=\"color:aliceblue; font-weight: bold;\"> {} volt</p>\n\t\t</div>\n\t\t<div class=\"item\" style=\"grid-row: 1 / 2; grid-column: 2 / 3;\">\n\t\t\t<h2>Voltage 2</h2>\n\t\t\t<img src=\"static/img/volt.png\" alt=\"Battery\">\n\t\t\t<div class=\"progressbar\">\n\t\t\t\t<progress max=\"100\" value=\"75\" style=\"accent-color: {};\"></progress>\n\t\t\t</div>\n\t\t\t<p style=\"color:aliceblue; font-weight: bold;\"> {}volt</p>\n\t\t</div>\n\t\t<div class=\"item\" style=\"grid-row: 1 / 2; grid-column: 3 / 4;\">\n\t\t\t<h2>Current</h2>\n\t\t\t<img src=\"static/img/ampere.png\" alt=\"Battery\">\n\t\t\t<div class=\"progressbar\">\n\t\t\t\t<progress max=\"100\" value=\"70\" style=\"accent-color: {};\"></progress>\n\t\t\t</div>\n\t\t\t<p style=\"color:aliceblue; font-weight: bold;\"> {} mA</p>\n\t\t</div>\n\t\t<div class=\"item\" style=\"grid-row: 2 / 3; grid-column: 1 / 2;\">\n\t\t\t<h2>SOC</h2>\n\t\t\t<img src=\"{}\" alt=\"Battery\">\n\t\t\t<div class=\"progressbar\">\n\t\t\t\t<progress max=\"100\" value=\"40\" style=\"accent-color: {};\"></progress>\n\t\t\t</div>\n\t\t\t<p style=\"color:aliceblue; font-weight: bold;\"> {} %</p>\n\t\t</div>\n\t\t<div class=\"item\" style=\"grid-row: 2 / 3; grid-column: 2 / 3;\">\n\t\t\t<h2>Temperature</h2>\n\t\t\t<img src=\"static/img/thermometer.png\" alt=\"Thermometer\">\n\t\t\t<div class=\"progressbar\">\n\t\t\t\t<progress max=\"100\" value=\"90\" style=\"accent-color: {};\"></progress>\n\t\t\t</div>\n\t\t\t<p style=\"color:aliceblue; font-weight: bold;\"> {} °C</p>\n\t\t</div>\n\t\t<div class=\"item\" style=\"grid-row: 2 / 3; grid-column: 3 / 4;\">\n\t\t\t<h2>SOH</h2>\n\t\t\t<img src=\"{}\" alt=\"Battery\">\n\t\t\t<div class=\"progressbar\" >\n\t\t\t\t<progress max=\"100\" value=\"90\" style=\"accent-color: {};\"></progress>\n\t\t\t</div>\n\t\t\t<p style=\"color:aliceblue; font-weight: bold;\"> {} %</p>\n\t\t</div>\n\t</div>\n</body>\n</html>".format(
							ONCLICK_DASHBOARD,
							ONCLICK_HISTORY,
							setVoltageColor(v1), v1,
							setVoltageColor(v2), v2,
							setVoltageColor(v3), v3,
							setCurrentColor(i), i,
							setBatteryLevelImg(soc), setBatteryColor(soc), soc,
							setTemperatureColor(t), t,
							setBatteryLevelImg(soh), setBatteryColor(soh), soh
	)
