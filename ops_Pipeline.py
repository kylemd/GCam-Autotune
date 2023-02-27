import cv2
import os
import pyiqa
import time
import torch

import ops_ADB as ctrl
import ops_Patcher as patch
from ProjectPepega import arm as hex2arm

# Start device

def initialise_camera(device,argsDict):
    package = argsDict['appPackage']
    activity = argsDict['appActivity']

    ctrl.StartCamera(device,package,activity)
    time.sleep(1)
    cam_running = ctrl.CheckAppRunning(device,package)

    if cam_running == True:
        return device
    else:
        return Exception

def initialise_iqa(iqaMetric):
	iqaMetric = pyiqa.create_metric(iqaMetric, device=torch.device('cuda'))
	metricDirection = iqaMetric.lower_better
	return iqaMetric, metricDirection

def img_pipeline(device,argsDict,tuneDict,newValue,iqaMetric):
    try:
        # Frida method
        # time.sleep(1)
        # hexnew = patch.patch_ram(patchscript,tunable,newvalue)

        # File method
        hexValue = patch.patch_file(device,argsDict['appLibPath'],
                                    tuneDict,newValue)
        
        initialise_camera(device,argsDict)
        
        # Send click to centre of screen to focus and adjust exposure
        device.click(((2340/2)-150), (1080/2))
        time.sleep(3)
        ctrl.TakePhoto(device)

        directory = argsDict['remoteOutputDir']
        package = argsDict['appPackage']

        remoteFile = ctrl.WaitForNewFile(device,directory,format,package)
        localFile = ctrl.RetrievePhoto(device,remoteFile,directory,format)
        
        iqScore = iq_test(localFile,iqaMetric)

        return localFile, hexValue, iqScore

    except Exception:
        return Exception, Exception, Exception

def iq_test(image,iqaMetric):

    if len(image) > 1:
        # For full reference tests, not yet implemented
        ref_image = cv2.imread(image[0])
        test_image = cv2.imread(image[1])
    else:
        test_image = cv2.imread(image[0])

    # Process the image so we can detect test chart border and crop
    gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)	
    gaussian = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
    edges = cv2.Canny(gaussian,100,200)
    contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contour = max(contours, key = len)	
    x, y, w, h = cv2.boundingRect(contour)
	
    cropped=test_image[y:y+h,x:x+w]
    croppedTensor=torch.tensor(cropped).permute(2,0,1)[None,...]/255.

    iqScore = iqaMetric(croppedTensor).item()
    cv2.imwrite(image, cropped)

    return iqScore