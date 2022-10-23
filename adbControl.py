import os
import time
import adbutils



###############################################################################
# Connect phone via USB ADB
###############################################################################

def ConnectDevice(device):

    # #Wait for user to connect
    # print('Ensure your device is plugged in via USB and the only Android device connected. Then press enter.')
    # input()

    #Run ADB server and connect to device
    try:
        adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
    except:
        print('Something went wrong with adb. Check you installed dependencies and have ADB installed.')

    #While device isn't connected, keep checking
    adb_timeout = time.time() + 60
    while time.time() < adb_timeout: 
        if adb.device_list() == '':
            print('Device not connected. Trying again in 5 seconds.')
            time.sleep(5)
        else:
            print(adb.device_list())
            device = adb.device()
            break

    # #Elevate to root permissions
    # print("Requesting root permissions. If this fails the script will be terminated.")
    # device.root()
    
    return device

###############################################################################
# Start the camera and make sure it doesn't crash
###############################################################################

def AppActions(device,package,action,activity):

    if action == 'CameraStart':
        #Clear logcat so errors can be isolated
        device.shell("logcat --clear")

        #Start the camera
        print('Starting camera')
        device.shell("am start -n {}/{}".format(package,activity))

    if action == 'TakePhoto':
        #Take a photo
        print('Taking a photo...')
        device.shell("input keyevent KEYCODE_CAMERA")
        time.sleep(10)

    #Checking to see if the camera is still running

    print('Checking to see if camera is still running...')
    camrunning = device.shell("ps | grep '{}'".format(package))

    if "bad " in camrunning:
        print('Camera appears to have crashed.')
        exit()


###############################################################################
# Copy newly created DNG to PC
###############################################################################

#Check for newly created file
def PullImage(device,destdir):
    srcdng = device.shell("logcat -e Moving -e dng -d")
    srcdng = srcdng.split(" to ")[-1]

    #Pull new dng and name in appropriately
    device.sync.pull(srcdng, destdir)