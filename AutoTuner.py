import ops_libValuesAPI as LibAPI
import ops_ADB as Ctrl
import ops_Pipeline
import ops_TestSingleParam as Experiment

# Dict for paths, app package names etc. Passing them as individual params gets messy
args_dict = {
    "appPackage": "com.androidcamera.ucvm",
    "appActivity": "com.android.camera.CameraLauncher",
    "appLibPath": "/data/app/~~llWJ_SRKQNirWRD_BbRrRQ==/com.androidcamera.ucvm-HMg6ssZerwWgbbugTkUOeQ==/lib/arm64/libgcastartup.so",
    "remoteOutputDir": "/sdcard/DCIM/Camera",
    "remoteOutputExt": "jpg",
    "iqaMethod": "pi",
    "outputDir": ".\\output"
}

# Copy and paste a value from Rivovs API here if you want to test just one specific value
testParam = [{
    "id": 106,
    "name": "Sharp gain",
    "lib_version": "8.4.400_rc19",
    "arm_type": "ARMFLT",
    "disasm": "movz w8, #0xbf80, lsl #16",
    "added_on": "2022-07-01T09:39:05.875276",
    "description": "",
    "address": "01FBC294",
    "length_in_lib": 4,
    "hex_original": "08F0B752",
    "extracted_value": "-1",
    "added_by": 1,
    "range": [0, 65535]
}]

device = Ctrl.connect_device()

if device == 0:
    print("Device not detected before running. Make sure it is running and stable and try again.")
    exit()
else:
    print(str(device))

if len(testParam) != 0:
    lib_dict = testParam
else:
    lib_dict = LibAPI.get_lib_values()

iqaMetric, metricDirection = ops_Pipeline.initialise_iqa(args_dict['iqaMethod'])

Experiment.run_optimisation(device, args_dict, lib_dict)
