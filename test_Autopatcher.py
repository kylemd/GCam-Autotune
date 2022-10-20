import libValuesAPI
import fridaLibPatcher
import adbControl
import frida
import time

from ax import optimize

lib_params = libValuesAPI.getRangeDict()
device = adbControl.ConnectDevice('c0a691ea')
package_name = 'org.codeaurora.snapcam'

address = "02E94258"
type = "float"
lower = float("0")
upper = float("65535")

# for i in lib_params:
#         if i['range'] != '':
#                 if i['address'] == '02E94258':
#                         times = round((int(i['range'][1]) - int(i['range'][0])) / 30)
#                         for x in range(times):
#                                 fridaLibPatcher.patchAndSnap(package_name,i['address'],i['hex_original'],int(x))
#                                 adbControl.AppActions(device,'TakePhoto')
#                                 time.sleep(10000)
        