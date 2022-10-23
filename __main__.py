import libValuesAPI
import fridaLibPatcher

cameraPackage = 'com.shamim.cam'

libParams = libValuesAPI.get_lib_values()
patchScript = fridaLibPatcher.load_hook(cameraPackage)
fridaLibPatcher.patch_and_snap(patchScript, libParams)