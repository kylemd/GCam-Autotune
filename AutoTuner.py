import ops_libValuesAPI as LibAPI
import ops_ADB as Ctrl
import ops_Pipeline
import ops_TestSingleParam as Experiment

# Dict for paths, app package names etc. Passing them as individual params gets messy
args_dict = {
    "appPackage": "com.androidcamera.ucvm",
    "appActivity": "com.android.camera.CameraLauncher",
    "appLibPath": "/data/app/~~PCtiWutFb5qvEp1roy5L8A==/com.androidcamera.ucvm-18cmbDEut5OwOxVvwQA4sQ==/lib/arm64"
                  "/libgcastartup.so",
    "remoteOutputDir": "/sdcard/DCIM/Camera",
    "remoteOutputExt": "jpg",
    "iqaMethod": "brisque",
    "outputDir": ".\\output"
}

# >>> print(pyiqa.list_models("NR")) 
# ['brisque', 'clipiqa', 'clipiqa+', 'cnniqa', 'dbcnn', 'fid', 'ilniqe', 'maniqa', 'musiq', 'musiq-ava', 'musiq-koniq', 'musiq-paq2piq', 'musiq-spaq', 'nima', 
#  'nima-vgg16-ava', 'niqe', 'nrqm', 'paq2piq', 'pi', 'tres', 'tres-flive', 'tres-koniq']

# Copy and paste a value from Rivovs API here if you want to test just one specific value
testParam = [{
    "id": 775,
    "name": "",
    "lib_version": "8.4.400_rc19",
    "arm_type": "ARMRPL",
    "disasm": "fdiv s9, s1, s10",
    "added_on": "2022-07-12T12:20:05.566349",
    "description": "",
    "address": "01ED2E58",
    "length_in_lib": 4,
    "hex_original": "29182A1E",
    "extracted_value": "",
    "range": [ -31, 31 ]
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

Experiment.run_optimisation(device, args_dict, lib_dict)
