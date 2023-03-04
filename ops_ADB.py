import os
import time
import adbutils
import threading

# set the maximum amount of time to wait for new_file
MAX_WAIT_TIME = 15


def connect_device():
    # #Wait for user to connect
    # print('Ensure your device is plugged in via USB. Then press enter.')
    # input()

    # Run ADB server and connect to device
    try:
        adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
        connected_devices = adb.list()
    except:
        print('Something went wrong with adb. Check you installed dependencies and have ADB installed.')
        exit()

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


def get_camera_package_name(device):
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


def start_camera(device, package, activity):
    device.shell("am start -n {}/{}".format(package, activity))


def take_photo(device):
    device.keyevent("KEYCODE_CAMERA")


def check_app_running(device, package):
    status = device.shell("pidof {}".format(package))

    if not status:
        return False
    else:
        return True


def get_photo_path(device, directory, pic_format):
    new_file = device.shell(
        "find {} -name '*.{}' -a -not -name '*pending*' -mtime -15s -mtime +2s".format(directory, pic_format))
    return new_file


def wait_for_new_file(device, output_dir, output_format, package):
    timeout = time.time() + 60  # 30 second timeout
    process_running = check_app_running(device, package)

    while process_running is True:
        if time.time() > timeout:
            return 0  # Timeout reached without finding new file

        process_running = check_app_running(device, package)  # Check variable again...not very elegant
        pathname = get_photo_path(device, output_dir, output_format)  # Check variable again...not very elegant

        if output_format in pathname:
            return pathname  # New file found

        time.sleep(1)  # Wait 1 second before checking again

    return 0  # process_running returned false, i.e. crashed


def pull_image(device, pathname, destfile):
    # Pull new dng and name in appropriately
    device.sync.pull(pathname, destfile)


def retrieve_photo(device, pathname, output_dir, output_format):
    filename = os.path.basename(pathname)
    pathname = output_dir + '/' + filename
    destfile = '.\\output\\' + str(filename)

    pull_image(device, pathname, destfile)
    device.shell(['rm', pathname])
    return destfile
