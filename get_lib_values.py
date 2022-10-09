import urllib.request
import json
import operator
import fridaLibPatcher

#def GetLibValues():

newvalue = '5'

requrl = 'http://152.67.78.6:8080/v2/addresses/by_version/?lib_version=8.4.400_rc19&allow_in_testing=true'
with urllib.request.urlopen(requrl) as req:
	input_dict = json.load(req)

input_dict.sort(key=operator.itemgetter('address'))

with open('libtunables.txt', 'w') as f:
	for x in input_dict:
		f.write(x['address'] + '|' + x['name'] + '\n')

for x in input_dict:
	if 'noise' in x['name']:
		fridaLibPatcher(x['address'],x['hex_original'],newvalue)
