import pprint, data.pys.routedata as routedata
import xml.etree.ElementTree as ET

allRoutesPathData = {} # this will be the big dictionary we store all data in
for route in routedata.allRoutes: # loop through all the routes
    allRoutesPathData[route] = [] # this will be a list of lists of {'lon':XXX, 'lat':XXX} dictonaries

    xmlName = 'data/xmls/routesData/pathData_'+(route)+'.xml'
    tree = ET.parse(xmlName)
    root = tree.getroot()
    for child in root[0]: # iterate over all the elements in the <route> element
        if child.tag != 'path':
            continue

        pathElement = []
        for point in child:
            pathElement.append({'lon': point.attrib['lon'], 'lat': point.attrib['lat']}) # append this point to the path
        allRoutesPathData[route].append(pathElement) # append the path to the main dictionary

# output all the data to a file named munipaths.py:
fo = open('data/pys/gspnspaths.py', 'w')
fo.write('gspnspaths = ' + pprint.pformat(allRoutesPathData))
fo.close()
