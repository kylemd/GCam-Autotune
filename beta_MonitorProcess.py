import threading
import time
import ops_ADB as ctrl

# set the maximum amount of time to wait for new_file
MAX_WAIT_TIME = 30

def check_app_running(device, package, result, should_exit):
    result[0] = ctrl.CheckAppRunning(device, package)
    if not result[0]:
        should_exit[0] = True

def poll_for_new_file(device, directory, format, result, should_exit):
    start_time = time.time()
    while True:
        if should_exit[0]:
            return
        new_file = ctrl.GetPhotoPath(device, directory, format)
        if new_file:
            result[0] = new_file
            return
        if time.time() - start_time > MAX_WAIT_TIME:
            result[0] = None
            return
        time.sleep(1)

def monitor_process(device, package, directory, format):
    # use a list to hold the results from the threads
    results = [None, None]

    # use a list to hold a shared variable to signal the threads to exit
    should_exit = [False]

    # create and start the threads
    app_running_thread = threading.Thread(target=check_app_running, args=(device, package, results, should_exit))
    app_running_thread.start()
    new_file_thread = threading.Thread(target=poll_for_new_file, args=(device, directory, format, results, should_exit))
    new_file_thread.start()

    # wait for the threads to finish
    app_running_thread.join()
    new_file_thread.join()

    # check the results
    if not results[0]:
        raise Exception("Process not running")
    if not results[1]:
        raise Exception("Timed out waiting for new file")
    return results[1]

# This version of the monitor_process function uses a shared variable should_exit to signal the new_file_thread to exit. 
# When the app_running_thread sets should_exit to True, the new_file_thread will exit its loop and return. 
# This ensures that the new_file_thread will stop polling for a new file as soon as the process stops running.

# You can call this function with the appropriate arguments to monitor the process and detect errors. 
# It will run the two functions simultaneously and terminate the new_file_thread as soon as the app_running_thread returns 0.