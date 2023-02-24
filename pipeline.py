import os
import time
import ops_ADB as ctrl
import ops_FridaPatcher as patch
import ops_Vision as iqa



# Start device

def initialise_device(package,activity):
    device = ctrl.ConnectDevice()
    ctrl.StartCamera(device,package,activity)                               #Need to change this to Frida boot instance
    cam_running = ctrl.CheckAppRunning(device,package)
    time.sleep(5)

    if cam_running == True:
        return device
    else:
        return 0

def generate(device,package,directory,format,tunable,newvalue):      #Passing vars here?
    try:
        patchscript = patch.load_hook(package)
        time.sleep(5)
        patch.PatchRAM(patchscript,tunable,newvalue)
        ctrl.TakePhoto(device)
        time.sleep(5)
        # file = ctrl.ProcessMonitor(device,package,directory,format)
        file = ctrl.WaitForNewFile(device, directory, format, package)
        localfile = ctrl.RetrievePhoto(device,file,directory,format)
        score = iqa.IQTest(localfile)
        return score
    except:
        return 999999999999