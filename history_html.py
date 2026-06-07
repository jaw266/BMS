from flask import request
from urllib.parse import urlparse
import htmlParser

def history(mesures):
	URL			= request.url
	URL_BASE	= f"{urlparse(URL).scheme}://{urlparse(URL).netloc}"

	ONCLICK_DASHBOARD	= f'''onclick="window.location.href='{URL_BASE}/';"'''
	ONCLICK_HISTORY		= f'''onclick="window.location.href='{URL_BASE}/history';"'''

	parsedHistoryTable = htmlParser.parseHistoryTable(mesures)
	return '''<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset=\"UTF-8\" >\n\t<title>Battery Dashboard</title>\n\t<link rel=\"stylesheet\" href=\"static/style.css\">\n\t\t<style>\n\t\t\t.input-group {{\n\t\t\t  display: inline-block;\n\t\t\t  margin: 0 10px;\n\t\t\t}}\n\t\t  </style></head>\n<body style=\"background-color: #404040;\">\n\t<nav>\n\t\t<div class=\"navbar-left\">\n\t\t  <button class=\"btn-dashboard\" {}>Dashboard</button>\n\t\t</div>\n\t\t<div class=\"navbar-right\">\n\t\t  <button class=\"btn-history\" {}>History</button>\n\t\t</div>\n\t</nav>\n\t<form action=\"\" method=\"get\" style =\"text-align: center;\">\n\t  <h1 style=\"color:aliceblue\">Choisir date:</h1>\n\t  <div class=\"input-group\">\n\t\t<h3>De :</h3>\n\t\t<input type=\"datetime-local\" id=\"DateDebut\" name=\"DateDebut\">\n\t  </div>\n\t  <div class=\"input-group\">\n\t\t<h3>Jusqu'a :</h3>\n\t\t<input type=\"datetime-local\" id=\"DateFin\" name=\"DateFin\">\n\t  </div>\n\t  <br> </br>\n\t  <center><input type=\"submit\" id=\"date-form\"></center>\n\t</form>\n\t<br>\n\t<br>\n\t<br>\n\t<table border=\"2\" bordercolor=\"#FFF\" width=\"40%\" cellspacing=\"2\" style=\"margin: auto;\">\n\t\t<tr style=\"color:#FFF;font-size:30px;\"><th colspan=\"8\">Mesures</th></tr>\n\t\t<tr style=\"font-size:22px; white-space: nowrap;\" >\n\t\t\t<th>Tension 1</th>\n\t\t\t<th>Tension 2</th>\n\t\t\t<th>Tension Totale</th>\n\t\t\t<th>Courant</th>\n\t\t\t<th>Temperature</th>\n\t\t\t<th>SOC</th>\n\t\t\t<th>SOH</th>\n\t\t\t<th>Date Heure</th>\n\t\t</tr>\n\t{}</table></body>\n</html>\n'''.format(
		ONCLICK_DASHBOARD,
		ONCLICK_HISTORY,
		parsedHistoryTable
	)