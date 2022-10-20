import pyiqa
import torch

ref_image = 'C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Assets/Reference/focuschart_compressed.jpg'
test_image = "C:/Users/kyle/Development/AutoTune_New/GCam-Autotune/Assets/Tests/Examples/20221005_133532_kylemd_bl0adc.jpg"


# list all available metrics
models = ['brisque', 'dbcnn', 'ilniqe', 'lpips-vgg', 'mad', 'maniqa', 
          'musiq', 'musiq-ava', 'musiq-koniq', 'musiq-paq2piq', 
          'musiq-spaq', 'nima', 'niqe', 'nrqm', 'paq2piq', 'pi']

for i in models:
    if i != 'fid':
        iqa_metric  = pyiqa.create_metric(i, device=torch.device('cuda'))
        score_nr = iqa_metric(test_image)
        print(i + " | " + str(iqa_metric.lower_better) + " | " + str(score_nr))
        torch.cuda.empty_cache()


# Note that gradient propagation is disabled by default. set as_loss=True to enable it as a loss function.
# iqa_loss = pyiqa.create_metric('lpips', device=torch.device('cuda'), as_loss=True)

# example for iqa score inference
# Tensor inputs, img_tensor_x/y: (N, 3, H, W), RGB, 0 ~ 1
# score_fr = iqa_metric(img_tensor_x, img_tensor_y)
# score_nr = iqa_metric(img_tensor_x)
# pyiqa.

# img path as inputs.
# score_fr = iqa_metric(ref_image, test_image)

# For FID metric, use directory or precomputed statistics as inputs
# refer to clean-fid for more details: https://github.com/GaParmar/clean-fid
# fid_metric = pyiqa.create_metric('fid')
# score = fid_metric('./ResultsCalibra/dist_dir/', './ResultsCalibra/ref_dir')
# score = fid_metric('./ResultsCalibra/dist_dir/', dataset_name="FFHQ", dataset_res=1024, dataset_split="trainval70k")