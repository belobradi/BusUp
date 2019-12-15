import data.pys.gspnspaths as gspnspaths
import random

fo = open('data/javas/polylineJAVA.java', 'w')

for route in gspnspaths.gspnspaths.keys():

    for path in gspnspaths.gspnspaths[route]:
        latlngJava = []
        for point in path:
            latlngJava.append('new LatLng(%s, %s)' % (point['lat'], point['lon']))
        latlngJava = ', '.join(latlngJava)

        polylineJava = """	Polyline line_%s = Map.addPolyline(new PolylineOptions()
	.add(%s)
	.width(5)
	);
""" % (route, latlngJava)

        fo.write(polylineJava)
fo.close()