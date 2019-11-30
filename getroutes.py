import xml.etree.ElementTree as ET

# open the file and read the contents
tree = ET.parse('data/xmls/routesName.xml')
root = tree.getroot()
routes = {}
for child in root:
    routes[child.attrib['tag']] = child.attrib['title']
#    print(child.attrib['tag'],child.attrib['title'])

import pprint
fo = open('data/pys/routedata.py','w')
fo.write('allRoutes = ' + pprint.pformat(routes))
fo.close()
