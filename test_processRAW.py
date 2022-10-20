import imageio.v3 as iio
import cv2

ref_image = 'C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Assets/Reference/focuschart_compressed.jpg'
test_image = "C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Assets/Tests/Examples/20221005_133532_kylemd_bl0adc.jpg"
test_image_raw = "C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Assets/Tests/Examples/20221005_133532_kylemd_bl0adc.dng"

img = iio.imread(test_image) #RAW colors aren't right
# cv2.imshow("original", img)
# cv2.waitKey()

