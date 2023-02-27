import os
import time
import ops_ADB as ctrl
import ops_FridaPatcher as patch
import ops_Vision as iqa
from ProjectPepega import arm as hex2arm

# Start device

def initialise_camera(device,package,activity):
    ctrl.StartCamera(device,package,activity)
    time.sleep(1)
    cam_running = ctrl.CheckAppRunning(device,package)

    if cam_running == True:
        return device
    else:
        return 0, 0

def patch_libs(device,libpath,tunable,newvalue):
    address = tunable['address']
    hexvalue = hex2arm.generate_hex(tunable['hex_original'], newvalue)

    if hexvalue == None:
        hexvalue = hex(int(newvalue))
    else:
        hexvalue = swap_endianness(hexvalue.upper())

    device.shell(["python","/sdcard/autotune_patcher.py",libpath,address,hexvalue])

def generate(device,patchscript,package,directory,format,tunable,newvalue,metric):      #Passing vars here?
    try:
        libpath = '/sdcard/libgcastartup.so'
        patch_libs(libpath,tunable,newvalue)
        initialise_camera(device,package,activity)
        #device.click(((2340/2)-150), (1080/2))
        time.sleep(3)
        ctrl.TakePhoto(device)
        file = ctrl.WaitForNewFile(device, directory, format, package)
        localfile = ctrl.RetrievePhoto(device,file,directory,format)
        
        score = iqa.IQTest(localfile,metric)
        return localfile, hexnew, score

    except Exception:
        return Exception, Exception, Exception