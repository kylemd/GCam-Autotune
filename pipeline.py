import os
import time
import ops_ADB as ctrl
import ops_FridaPatcher as patch
import ops_Vision as iqa
from ProjectPepega import arm as hex2arm

# Start device

def initialise_camera(device,package,activity):
    ctrl.StartCamera(device,package,activity)
    time.sleep(1)
    cam_running = ctrl.CheckAppRunning(device,package)

    if cam_running == True:
        return device
    else:
        return 0, 0

def initialise_iqa(metric):
	iqa_metric = pyiqa.create_metric(metric, device=torch.device('cuda'))
	metric_direction = iqa_metric.lower_better
	return iqa_metric, metric_direction

def patch_libs(device,libpath,tunable,newvalue):
    address = tunable['address']
    hexvalue = hex2arm.generate_hex(tunable['hex_original'], newvalue)

    if hexvalue == None:
        hexvalue = hex(int(newvalue))
    else:
        hexvalue = swap_endianness(hexvalue.upper())

    device.shell(["python","/sdcard/autotune_patcher.py",libpath,address,hexvalue])

def generate(device,patchscript,package,directory,format,tunable,newvalue,metric):      #Passing vars here?
    try:
        libpath = '/sdcard/libgcastartup.so'
        patch_libs(libpath,tunable,newvalue)
        initialise_camera(device,package,activity)
        #device.click(((2340/2)-150), (1080/2))
        time.sleep(3)
        ctrl.TakePhoto(device)
        file = ctrl.WaitForNewFile(device, directory, format, package)
        localfile = ctrl.RetrievePhoto(device,file,directory,format)
        
        score = iqa.IQTest(localfile,metric)
        return localfile, hexnew, score

    except Exception:
        return Exception, Exception, Exception

def IQTest(image,metric):

	test_image = cv2.imread(image)

	gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)	
	gaussian = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
	edges = cv2.Canny(gaussian,100,200)
	contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	contour = max(contours, key = len)
		
	x, y, w, h = cv2.boundingRect(contour)

	# Py-IQA module method
	
	# Display cropped image
	
	cropped=test_image[y:y+h,x:x+w]
	cropped_tensor=torch.tensor(cropped).permute(2,0,1)[None,...]/255.
	score_nr = metric(cropped_tensor).item()
	
	cv2.imwrite(image, cropped)
	return score_nr