import cv2
import pyiqa
import torch
# from process_raw import DngFile
from ax import optimize
import numpy as np
import math
import imageio

ref_image = 'C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Assets/Reference/focuschart_compressed.jpg'
test_image = "C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Assets/Tests/Examples/20221005_133532_kylemd_bl0adc.jpg"

def cropTestChart():
  #Kanged from https://learnml.today/opencv-automatic-cropping-and-image-warping-2


  new_photo = cv2.imread(test_image, 0)
  orig_image = cv2.imread(ref_image, 0)
  orig_image_rgb = cv2.imread(ref_image)

  try:
      surf = cv2.KAZE_create()
      kp1, des1 = surf.detectAndCompute(new_photo, None)
      kp2, des2 = surf.detectAndCompute(orig_image, None)
  except cv2.error as e:
      raise e
    
  bf = cv2.BFMatcher()
  matches = bf.knnMatch(des1, des2, k=2)
    
  # store all the good matches as per Lowe's ratio test.
  good = []
  for m, n in matches:
      if m.distance < 0.7 * n.distance:
          good.append(m)

  # if less then 10 points matched -> not the same images or higly distorted 
  MIN_MATCH_COUNT = 10
  if len(good) > MIN_MATCH_COUNT:
      src_pts = np.float32([kp1[m.queryIdx].pt for m in good
                              ]).reshape(-1, 1, 2)
      dst_pts = np.float32([kp2[m.trainIdx].pt for m in good
                              ]).reshape(-1, 1, 2)

      kp1_matched=([ kp1[m.queryIdx] for m in good ])
      kp2_matched=([ kp2[m.trainIdx] for m in good ])   

      matches = cv2.drawMatches(new_photo,kp1,orig_image,kp2, good,None, flags=2)
      plt.figure(figsize=(20,10))
      plt.axis('off')
      plt.imshow(matches),plt.show()   

  img_rgb = cv2.imread(test_image)
  img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
  template = cv2.imread(ref_image, cv2.IMREAD_GRAYSCALE)
  w, h = template.shape
  res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
  _, _, _, maxLoc=cv2.minMaxLoc(res)
  cv2.rectangle(img_rgb, maxLoc, (maxLoc[0]+h, maxLoc[1]+w), (0, 255, 255), 2)
  cv2.imshow('Detected', img_rgb)
  crop_img = img_rgb[maxLoc[1]:maxLoc[1]+w, maxLoc[0]:maxLoc[0]+h, :] 
  cv2.imshow("cropped", crop_img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()