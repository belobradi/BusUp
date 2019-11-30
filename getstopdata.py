import pprint, data.pys.routedata as routedata
import xml.etree.ElementTree as ET

allRoutesStopData = {} # this will be the big dictionary we store all data in
for route in routedata.allRoutes: # loop through all the routes
    allRoutesStopData[route] = [] # this will be a list of lists of {'lon':XXX, 'lat':XXX} dictonaries

    xmlName = 'data/xmls/routesData/pathData_'+(route)+'.xml'
    tree = ET.parse(xmlName)
    root = tree.getroot()
    for child in root[0]: # iterate over all the elements in the <route> element
        if child.tag != 'stop':
            continue

        allRoutesStopData[route].append({'title': child.attrib['title'],
                                         'lon': child.attrib['lon'],
                                         'lat': child.attrib['lat'],
                                         'stopId': child.attrib['stopId']}) # append the stop

# output all the data to a file named munipaths.py:
fo = open('data/pys/gspnsstops.py', 'w')
fo.write('gspnsstops = ' + pprint.pformat(allRoutesStopData))
fo.close()
