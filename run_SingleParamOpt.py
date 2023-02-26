import ops_libValuesAPI as libapi
import ops_ADB as ctrl
import pipeline
import shutil

from ax import optimize
# from ax.plot.contour import plot_contour
# from ax.utils.notebook.plotting import render, init_notebook_plotting

package = 'com.shamim.cam'
activity = "com.android.camera.CameraLauncher"
output_dir = '/sdcard/DCIM/Camera'
output_format = 'jpg'
results_array = []
device, patchscript = pipeline.initialise_device(package,activity)
# init_notebook_plotting()

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
            localfile, hexnew, iqa_score = pipeline.generate(device,patchscript,package,output_dir,output_format,tunable,newvalue)

            #Move file so results are easier to view
            shutil.move(str(localfile),'.\\output\\{}_{}_{}.{}'.format(d['address'],iqa_score,newvalue,output_format))
            results_array.append([d['name'],d['address'],newvalue,hexnew, iqa_score, localfile])
            return {'iqa_score': iqa_score }
        except Exception:
            return Exception
        

    # Run the optimization
    best_parameters, best_score, _foo, _bar  = optimize(
        experiment_name="test",
        objective_name="iqa_score",
        evaluation_function=RunPatchTests,
        parameters=search_space,
        minimize=True,
        total_trials=50,
    )

    # render(plot_contour(model=test, param_x='x1', param_y='x2', metric_name='hartmann6'))
    # Return the best parameter value and corresponding score
    return best_parameters[hex_tunable], best_score[0]['iqa_score']

# Load the JSON dict - normally array of dict
#data = libapi.get_lib_values() 

if device == 0:
    print("Cam not detected before running. Make sure it is running and stable and try again.")
    exit()

data = [{
    "id": 178,
    "name": "Smoothness",
    "lib_version": "8.4.400_rc19",
    "arm_type": "ARM",
    "disasm": "fmov s0, #2.00000000",
    "added_on": "2022-07-01T09:39:06.408718",
    "description": "",
    "address": "01255FD4",
    "length_in_lib": 4,
    "hex_original": "0010201E",
    "extracted_value": "2",
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
    for i in results_array:
        print(i)