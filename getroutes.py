import re
import os
import requests

os.system("curl www.gspns.co.rs/mreza | grep \"button-linija tooltip\" > /tmp/routes")
os.system("curl www.gspns.co.rs/mreza | grep \"boje\[\" > /tmp/colors")
fr = open("/tmp/routes", "r")
fc = open("/tmp/colors", "r")
os.system("rm /tmp/routes; rm /tmp/colors")

html_contentR = fr.read()
html_contentC = fc.read()

rangeList = []
routeid = re.findall(r'id="(.*?)"', html_contentR)
rangeList.append(len(routeid))
titleid = re.findall(r'title="(.*?)"', html_contentR)
rangeList.append(len(titleid))
fullname = re.findall(r' > (.*?)</a>', html_contentR)
rangeList.append(len(fullname))
colors = re.findall(r'] = "(.*?)";', html_contentC)
rangeList.append(len(colors))

import json

data = {}
Routes = {}
routes_array = []
allroutestxt = ''
noid = 55 #min(rangeList)
for id in range(noid):
    ID = {}
    Name = {}
    Color = {}
    Coordinates = {}
    route_one = []
    routetxt = ''

    path = "http://www.gspns.co.rs/mreza-get-linija-tacke?linija="+str(routeid[id])
    print(path)

    #find ID
    routetxt = routetxt+"\"ID\" : "+routeid[id]+", "

    #find Name
    routetxt = routetxt+"\"Name\" : \""+fullname[id].strip()+"\", "

    #find Color
    routetxt = routetxt+"\"Color\" : \""+colors[id]+"\", "

    #find Coordinates
    response = requests.get(path)
    data = json.loads(response.text)
    my_nums = re.findall('\d+\.?\d*', repr(data))
    my_nums_len = len(my_nums)
    matrix=''
    for i in range(0, my_nums_len, 2):
        for j in range(2):
            if j:
                matrix = matrix+my_nums[i+1]+' ]'
            else:
                matrix = matrix+'[ '+my_nums[i]+', '
        if (i+2 < my_nums_len):
            matrix=matrix+', '
    routetxt = routetxt+"\"Coordinates\" : [ "+matrix+" ]"
    allroutestxt = allroutestxt+"{ "+routetxt+" }"
    if (id+1 < noid):
        allroutestxt=allroutestxt+', '

allroutestxt="{\"Routes\" : ["+allroutestxt+"] }"

text_file = open("export/json/lineData.json", "w")
text_file.write(allroutestxt)
text_file.close()
