import cv2
import pyiqa
import torch
from process_raw import DngFile
from ax import optimize

def cropTestChart():
    #Kanged from https://stackoverflow.com/questions/65644498/crop-detected-image-via-opencv

    img_rgb = cv2.imread('Image_1.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
    template = cv2.imread('template.png', cv2.IMREAD_GRAYSCALE)
    w, h = template.shape
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    _, _, _, maxLoc=cv2.minMaxLoc(res)
    cv2.rectangle(img_rgb, maxLoc, (maxLoc[0]+h, maxLoc[1]+w), (0, 255, 255), 2)
    cv2.imshow('Detected', img_rgb)
    crop_img = img_rgb[maxLoc[1]:maxLoc[1]+w, maxLoc[0]:maxLoc[0]+h, :] 
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def rawProcess():
    #Kanged from https://github.com/DIYer22/process_raw example docs
    
    # Download raw.dng for test:
    # wget https://github.com/yl-data/yl-data.github.io/raw/master/2201.process_raw/raw-12bit-GBRG.dng
    dng_path = "./raw-12bit-GBRG.dng"

    dng = DngFile.read(dng_path)
    raw = dng.raw  # np.uint16
    raw_8bit = np.uint8(raw >> (dng.bit-8))
    cv2.imwrite("raw_8bit.png", raw_8bit)

    rgb1 = dng.postprocess()  # demosaicing by rawpy
    cv2.imwrite("rgb1.jpg", rgb1[:, :, ::-1])
    rgb2 = dng.demosaicing(poww=0.3)  # demosaicing with gamma correction
    cv2.imwrite("rgb2.jpg", rgb2[:, :, ::-1])
    DngFile.save(dng_path + "-save.dng", dng.raw, bit=dng.bit, pattern=dng.pattern)
    
def assessQuality():
    #Kanged from https://github.com/chaofengc/IQA-PyTorch example docs

    # list all available metrics
    print(pyiqa.list_models())

    # create metric with default setting
    iqa_metric = pyiqa.create_metric('lpips', device=torch.device('cuda'))
    # Note that gradient propagation is disabled by default. set as_loss=True to enable it as a loss function.
    iqa_loss = pyiqa.create_metric('lpips', device=torch.device('cuda'), as_loss=True)

    # create metric with custom setting
    iqa_metric = pyiqa.create_metric('psnr', test_y_channel=True, color_space='ycbcr').to(device)

    # check if lower better or higher better
    print(iqa_metric.lower_better)

    # example for iqa score inference
    # Tensor inputs, img_tensor_x/y: (N, 3, H, W), RGB, 0 ~ 1
    score_fr = iqa_metric(img_tensor_x, img_tensor_y)
    score_nr = iqa_metric(img_tensor_x)

    # img path as inputs.
    score_fr = iqa_metric('./ResultsCalibra/dist_dir/I03.bmp', './ResultsCalibra/ref_dir/I03.bmp')

    # For FID metric, use directory or precomputed statistics as inputs
    # refer to clean-fid for more details: https://github.com/GaParmar/clean-fid
    fid_metric = pyiqa.create_metric('fid')
    score = fid_metric('./ResultsCalibra/dist_dir/', './ResultsCalibra/ref_dir')
    score = fid_metric('./ResultsCalibra/dist_dir/', dataset_name="FFHQ", dataset_res=1024, dataset_split="trainval70k")
    
def autoExperiment():
    #Boilerplate from https://github.com/facebook/Ax docs
    
    best_parameters, best_values, experiment, model = optimize(
        parameters=[
          {
            "name": "x1",
            "type": "range",
            "bounds": [-10.0, 10.0],
          },
          {
            "name": "x2",
            "type": "range",
            "bounds": [-10.0, 10.0],
          },
        ],
        # Booth function
        evaluation_function=lambda p: (p["x1"] + 2*p["x2"] - 7)**2 + (2*p["x1"] + p["x2"] - 5)**2,
        minimize=True,
    )

    # best_parameters contains {'x1': 1.02, 'x2': 2.97}; the global min is (1, 3)