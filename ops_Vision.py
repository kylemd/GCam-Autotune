import cv2
import torch
import piq
 
def IQTest(image):

	test_image = cv2.imread(image)

	gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)	
	gaussian = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
	edges = cv2.Canny(gaussian,100,200)
	contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	contour = max(contours, key = len)
		
	x, y, w, h = cv2.boundingRect(contour)
		
	cropped=torch.tensor(test_image[y:y+h,x:x+w]).permute(2,0,1)[None,...]/255.
	brisque_index:torch.Tensor=piq.brisque(cropped,data_range=1.,reduction='none')

	return brisque_index.item()


test_image = "C:\\Users\\kyle\\Development\\AutoTune_New\\GCam-Autotune\\Assets\\Tests\\CVM_20230217_101211706.jpg"
score = IQTest(test_image)
print(score)