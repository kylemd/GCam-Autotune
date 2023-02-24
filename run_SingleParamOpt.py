import ops_libValuesAPI as libapi
import ops_ADB as ctrl
import pipeline
from ax import optimize

package = 'com.androidcamera.ucvm'
activity = "com.android.camera.CameraLauncher"
output_dir = '/sdcard/DCIM/Camera'
output_format = 'jpg'
device = pipeline.initialise_device(package,activity)

# Define the search space and black box function for one parameter
def OptimizeSingleParam(hex_tunable):
    tunable_data = next(d for d in data if d['address'] == hex_tunable)
    search_space = [{
        'name': hex_tunable,
        'type': 'range',
        'bounds': [tunable_data['range'][0], tunable_data['range'][1]],
        'value_type': 'float' if isinstance(tunable_data['range'][0], float) or isinstance(tunable_data['range'][1], float) else 'int',
    }]

    def RunPatchTests(params):
        newvalue = params[hex_tunable]
        tunable = d
        try:
            iqa_score = pipeline.generate(device,package,output_dir,output_format,tunable,newvalue)
        except Exception:
            print('Something went wrong.')
            return 999999999999
        return {'iqa_score': iqa_score }

    # Run the optimization
    best_parameters, best_score, _foo, _bar  = optimize(
        experiment_name="test",
        objective_name="iqa_score",
        evaluation_function=RunPatchTests,
        parameters=search_space,
        minimize=True,
        total_trials=20,
    )

    # Return the best parameter value and corresponding score
    return best_parameters[hex_tunable], best_score[0]['iqa_score']

# Load the JSON dict - normally array of dict
#data = libapi.get_lib_values() 

if device == 0:
    print("Cam not detected before running. Make sure it is running and stable and try again.")
    exit()

data = [{
    "id": 133,
    "name": "Sabre noise artifacts",
    "lib_version": "8.4.400_rc19",
    "arm_type": "ARMRPL",
    "disasm": "ldr s2, [x19, #8]",
    "added_on": "2022-07-01T09:39:06.103645",
    "description": "covariance_parameters DENOISE_GRADIENT_THRESHOLD",
    "address": "02813648",
    "length_in_lib": 4,
    "hex_original": "620A40BD",
    "added_by": 1,
    "range": [
      -31,
      31
    ]
  }] # First value in array - for testing

for d in data:
    hex_tunable = d['address']
    best_parameter, best_score = OptimizeSingleParam(hex_tunable)
    print(f"Best value for {hex_tunable}: {best_parameter}, Score: {best_score}")