import cv2
import torch
#import piq
import pyiqa
import numpy as np
import os

def initialise_iqa(metric):
	iqa_metric = pyiqa.create_metric(metric, device=torch.device('cuda'))
	metric_direction = iqa_metric.lower_better
	return iqa_metric, metric_direction

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

	
	# PIQ module method
	# cropped=torch.tensor(test_image[y:y+h,x:x+w]).permute(2,0,1)[None,...]/255.
	# brisque_index:torch.Tensor=piq.brisque(cropped,data_range=1.,reduction='none')

	# return brisque_index.item()

# print(pyiqa.list_models('NR'))
# iqa_metric = pyiqa.create_metric('musiq-koniq', device=torch.device('cuda'))
# print(iqa_metric.lower_better)
# test_image = "C:\\Users\\kyle\\Development\\AutoTune_New\\GCam-Autotune\\output\\01FBC818\\01FBC818_-0.00592041015625_-31.jpg"
# score = IQTest(test_image,iqa_metric)