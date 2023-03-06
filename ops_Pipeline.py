import time

import cv2
import pyiqa
import torch
import shutil

import ops_ADB as Ctrl

from ProjectPepega import arm as hex2arm
from pathlib import Path


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
        hex_value = patch_file(device, args_dict['appLibPath'],
                               tune_dict, new_value)

        initialise_camera(device, args_dict)

        # Send click to centre of screen to focus and adjust exposure
        # device.click(((2340 / 2) - 170), (1080 / 2) - 50)

        time.sleep(3)
        Ctrl.take_photo(device)

        output_directory = args_dict['remoteOutputDir']
        app_package = args_dict['appPackage']
        output_format = args_dict['remoteOutputExt']

        remote_file = Ctrl.wait_for_new_file(device, output_directory, output_format, app_package)
        local_file = Ctrl.retrieve_photo(device, remote_file, output_directory, output_format)

        Ctrl.stop_camera(device, app_package)

        iq_score = iq_test(local_file, iqa_metric)

        print(new_value, iq_score)

        # Build output directory names
        local_output = '{}\\{}'.format(args_dict['outputDir'], tune_dict['address'])

        # Create output path if it doesn't exist
        Path(local_output).mkdir(parents=True, exist_ok=True)

        # Move file so results are easier to view
        ext = args_dict['remoteOutputExt']
        shutil.move(str(local_file), '{}\\{}_{}.{}'.format(local_output, iq_score, new_value, ext))

        return hex_value, iq_score

    except Exception:
        return Exception, Exception


# Patch lib file on device using in-built Linux GNU tools
def patch_file(device, libpath, tunedict, newvalue):
    hex_original = tunedict['hex_original']
    hex_size = int(tunedict['length_in_lib'])

    hex_value = hex2arm.generate_hex(hex_original, newvalue)
    if hex_value is None:
        hex_value = hex(int(newvalue))

    dec_address = int(tunedict['address'], 16)

    patch_cmd = "echo '{}' | xxd -r -p | dd of={} bs=1 seek={} count={} conv=notrunc".format(
        hex_value, libpath, dec_address, hex_size)

    device.shell(['su', '-c', patch_cmd])

    return hex_value


def iq_test(image, iqa_metric):
    test_image = cv2.imread(image)

    image_tensor = torch.tensor(test_image).permute(2, 0, 1)[None, ...] / 255.

    iq_score = iqa_metric(image_tensor).item()

    return iq_score
