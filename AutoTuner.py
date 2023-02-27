import ops_libValuesAPI as lib_api
import ops_ADB as ctrl
import ops_Pipeline
import ops_TestSingleParam as experiment

# Dict for paths, app package names etc. Passing them as individual params gets messy
argsDict={
    "appPackage": "com.shamim.cam",
    "appActivity": "com.android.camera.CameraLauncher",
    "appLibPath": "/data/app/~~-UD-FEAEYaK4LJ3ChnTM4w==/com.shamim.cam-eV5BypJR_YgDczL59zuV_g==/lib/arm64/libgcastartup.so",
    "remoteOutputDir": "/sdcard/DCIM/Camera",
    "remoteOutputExt": "jpg",
    "iqaMethod": "pi",
    "outputDir": ".\\output"
}

# Copy paste a value from Rivs API here if you want to test just one specific value
testParam={
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
    "range": [0,65535]
}

def main():
    device = ctrl.ConnectDevice()

    if device == 0:
        print("Cam not detected before running. Make sure it is running and stable and try again.")
        exit()

    if len(testParam) is not 0:
        libDict = testParam
    else:
        libDict = lib_api.get_lib_values() 

    iqaMetric,metricDirection = ops_Pipeline.initialise_iqa(argsDict['iqaMethod'])

    experiment.run_optimisation(device,argsDict,libDict)

    