import xml.etree.ElementTree as ET
import pprint
import pathlib

# open the file and read the contents
tree = ET.parse('data/xmls/routesName.xml')
root = tree.getroot()
routes = {}
for child in root:
    routes[child.attrib['tag']] = child.attrib['title']

pathlib.Path('data/pys').mkdir(parents=True, exist_ok=True)

fo = open('data/pys/routedata.py','w')
fo.write('allRoutes = ' + pprint.pformat(routes))
fo.close()
