import urllib.request
import json
import operator
import fridaMemoryMonitor

#def GetLibValues():

requrl = 'http://152.67.78.6:8080/v2/addresses/by_version/?lib_version=8.4.400_rc19&allow_in_testing=true'
with urllib.request.urlopen(requrl) as req:
	input_dict = json.load(req)

input_dict.sort(key=operator.itemgetter('address'))

libvalues = list()

for x in input_dict:
	libvalues.append('0x' + x['address'] + "," + x['hex_original'])

fridaMemoryMonitor.watchInMemory(libvalues)