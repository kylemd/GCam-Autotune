import time

import cv2
import pyiqa
import torch

import ops_ADB as Ctrl
import ops_Patcher as Patch


# Start device

def initialise_camera(device, argsdict):
    package = argsdict['appPackage']
    activity = argsdict['appActivity']

    Ctrl.start_camera(device, package, activity)
    time.sleep(1)
    cam_running = Ctrl.check_app_running(device, package)

    if cam_running:
        return device
    else:
        return Exception


def initialise_iqa(iqa_metric):
    iqa_metric = pyiqa.create_metric(iqa_metric, device=torch.device('cuda'))
    metric_direction = iqa_metric.lower_better
    return iqa_metric, metric_direction


def img_pipeline(device, args_dict, tune_dict, new_value, iqa_metric):
    try:
        # Frida method
        # time.sleep(1)
        # hexnew = Patch.patch_ram(patchscript,tunable,newvalue)

        # File method
        hex_value = Patch.patch_file(device, args_dict['appLibPath'],
                                    tune_dict, new_value)

        initialise_camera(device, args_dict)

        # Send click to centre of screen to focus and adjust exposure
        device.click(((2340 / 2) - 150), (1080 / 2))
        time.sleep(3)
        Ctrl.take_photo(device)

        directory = args_dict['remoteOutputDir']
        package = args_dict['appPackage']

        remote_file = Ctrl.wait_for_new_file(device, directory, format, package)
        local_file = Ctrl.retrieve_photo(device, remote_file, directory, format)

        iq_score = iq_test(local_file, iqa_metric)

        return local_file, hex_value, iq_score

    except Exception:
        return Exception, Exception, Exception


def iq_test(image, iqa_metric):
    if len(image) > 1:
        # For full reference tests, not yet implemented
        ref_image = cv2.imread(image[0])
        test_image = cv2.imread(image[1])
    else:
        test_image = cv2.imread(image[0])

    # Process the image so we can detect test chart border and crop
    gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray, (3, 3), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(gaussian, 100, 200)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contour = max(contours, key=len)
    x, y, w, h = cv2.boundingRect(contour)

    cropped = test_image[y:y + h, x:x + w]
    cropped_tensor = torch.tensor(cropped).permute(2, 0, 1)[None, ...] / 255.

    iq_score = iqa_metric(cropped_tensor).item()
    cv2.imwrite(image, cropped)

    return iq_score
