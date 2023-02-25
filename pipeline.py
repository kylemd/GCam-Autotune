import os
import time
import ops_ADB as ctrl
import ops_FridaPatcher as patch
import ops_Vision as iqa



# Start device

def initialise_device(package,activity):
    device = ctrl.ConnectDevice()
    ctrl.StartCamera(device,package,activity)
    time.sleep(1)
    patchscript = patch.load_hook(package)
    cam_running = ctrl.CheckAppRunning(device,package)

    if cam_running == True:
        return device, patchscript
    else:
        return 0, 0

def generate(device,patchscript,package,directory,format,tunable,newvalue):      #Passing vars here?
    try:
        hexnew = patch.PatchRAM(patchscript,tunable,newvalue)
        # device.click(((2340/2)-200), (1080/2))
        time.sleep(1)
        ctrl.TakePhoto(device)
        file = ctrl.WaitForNewFile(device, directory, format, package)
        localfile = ctrl.RetrievePhoto(device,file,directory,format)
        
        score = iqa.IQTest(localfile)
        return localfile, hexnew, score

    except Exception:
        return Exception, Exception, Exception