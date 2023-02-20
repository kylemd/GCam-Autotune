import os
import time
import adbutils
import threading
import ops_ADB as ctrl
import ops_FridaPatcher as patch

# Start device

def initialise_device():
    device = ctrl.ConnectDevice()
    ctrl.StartCamera(device,package,activity)                               #Need to change this to Frida boot instance
    cam_running = ctrl.CheckAppRunning(device,package)

    if cam_running == True:
        return 1
    else:
        return 0

def pipeline(device,package,activity,hexaddress,hexoriginal,newvalue):      #Passing vars here?
    ctrl.StartCamera(device,package,activity)                               #Change to Frida
    #Generate Frida value with value                                        
    patch.PatchRAM()                                                        #This is OK I think but 
    ctrl.TakePhoto(device)
    #This is where that code I generated the other day goes. If return 0 etc

    


#Generate value to write


# Take the photo

while cam_running == True:
    ctrl.TakePhoto(device)

    file = ctrl.RetrievePhoto(device,output_dir,output_format,package)