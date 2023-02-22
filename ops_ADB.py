import os
import time
import adbutils

def ConnectDevice():
    # #Wait for user to connect
    # print('Ensure your device is plugged in via USB. Then press enter.')
    # input()

    #Run ADB server and connect to device
    try:
        adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
        connected_devices = adb.list()
    except:
        print('Something went wrong with adb. Check you installed dependencies and have ADB installed.')

    try:
        if len(connected_devices) > 1:
            i = 0
            for device in connected_devices:
                print('[' + str(i) + ']\t' + str(device.serial))
                i = i + 1
            
            while True:
                try:
                    device_selection = int(input("Select which device you'd like to connect to."))
                    break
                except:
                    print("That's not a valid option!")

            selected_device = connected_devices[device_selection].serial
            device = adb.device(serial=selected_device)

        else:
            device = adb.device()
    except:
        print('Something wrong with adb or no devices connected')
        exit()

    print('Successfully connected to ' + str(device.serial))
    return device

def GetCameraPackageName(device):
    package_list = device.list_packages()

    for pkgindex, pkgname in enumerate(package_list):
        print('[' + str(pkgindex) + ']\t' + str(pkgname))

    while True:
        try:
            pkg_selection = int(input("Select your camera package:"))
            break
        except:
            print("That's not a valid option!")

    package_name = package_list[pkg_selection]
    return package_name

def StartCamera(device,package,activity):
    device.shell("am start -n {}/{}".format(package,activity))

def TakePhoto(device):
    device.keyevent("KEYCODE_CAMERA")

def CheckAppRunning(device,package):
    status = device.shell("pidof {}".format(package))
    
    if not status:
        return False
    else:
        return True

def GetPhotoPath(device,directory,format):
    new_file = device.shell("find {} -name '*.{}' -a -not -name '*pending*' -mtime -15s -mtime +2s".format(directory,format))
    return new_file

def WaitForNewFile(device, output_dir, output_format, package):
    
    timeout = time.time() + 60  # 30 second timeout
    process_running = CheckAppRunning(device,package)
    
    while process_running is True:
        if time.time() > timeout:
            return 0  # Timeout reached without finding new file
        
        process_running = CheckAppRunning(device,package) #Check variable again...not very elegant
        pathname = GetPhotoPath(device,output_dir,output_format) #Check variable again...not very elegant

        if output_format in pathname:
            return pathname  # New file found

        time.sleep(1)  # Wait 1 second before checking again

    return 0  # process_running returned false, i.e. crashed

def PullImage(device,pathname,destfile):
    #Pull new dng and name in appropriately
    device.sync.pull(pathname,destfile)

def RetrievePhoto(device,output_dir,output_format,package):
    pathname = WaitForNewFile(device,output_dir,output_format,package)

    filename = os.path.basename(pathname)
    pathname = output_dir + '/' + filename
    destfile = '.\\output\\' + str(filename)

    PullImage(device,pathname,destfile)
    return destfile