import cv2

def iq_test(image, iqa_metric):
    # if len(image) > 1:
    #     # For full reference tests, not yet implemented
    #     # ref_image = cv2.imread(image[0])
    #     test_image = cv2.imread(image[1])
    # else:
    test_image = cv2.imread(image)

    # Process the image, so we can detect test chart border and crop
    gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

    gaussian = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(gaussian, 100, 200)

    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )

    contour = max(contours, key=len)

    x, y, w, h = cv2.boundingRect(contour)

    cropped = test_image[y:y + h, x:x + w]
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cropped_tensor = torch.tensor(cropped).permute(2, 0, 1)[None, ...] / 255.

    iq_score = iqa_metric(cropped_tensor).item()
    cv2.imwrite(image, cropped)

    return iq_score

image = 'C:\\Users\\kyle\\Development\\AutoTune_New\\GCam-Autotune\\Misc_Tunable_Scripts\\OpenCV_Tests\\CVM_20230306_084013128.jpg'

test_image = cv2.imread(image)

# Process the image, so we can detect test chart border and crop
gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7, 7), 0.5)
edge = cv2.Canny(blur, 0, 50, 3)

contours, hierarchy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour = max(contours, key=len)

x, y, w, h = cv2.boundingRect(contour)

cropped = test_image[y:y + h, x:x + w]
cv2.imshow("cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()