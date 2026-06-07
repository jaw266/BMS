DEBUG	= True
PORT	= 3000
HOST	= '0.0.0.0'

DATABASE_URL = 'sqlite:///measurements.db'

Vmax	= 4.2
Vmin	= 2.7
VTotMax = 12.6
VTotMin = 8.1
Imax	= 110
Imin	= 10
Tmax	= 62
Tmin	= -20


VoltageLevel = {
	"BLUE"		: Vmin,
	"RED"		: Vmax
}

VoltageTotLevel = {
	"BLUE"		: VTotMax,
	"RED"		: VTotMin
}

CurrentLevel = {
	"BLUE"		: Imin,
	"RED"		: Imax
}


TemperatureLevel = {
	"BLUE"		: Tmin,
	"RED"		: Tmax
}

BatteryLevel = {
	"RED"		: 100 * 0.2,
	"ORANGE"	: 100 * 0.4,
	"YELLOW"	: 100 * 0.6,
	"GREEN"		: 100 * 0.8
}
