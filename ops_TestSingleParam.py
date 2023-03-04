import shutil
from pathlib import Path

from ax import optimize

import ops_Pipeline

resultsArray = []


# Define the search space and black box function for one parameter
def optimize_one_param(device, args_dict, tune_dict, hex_address):
    # tunableData = next(d for d in tunedict if d['address'] == hex_address)
    # low = tunableData['range'][0]
    # high = tunableData['range'][1]
    low = tune_dict['range'][0]
    high = tune_dict['range'][1]

    search_space = [{
        'name': hex_address,
        'type': 'range',
        'bounds': [low, high],
        'value_type': 'float' if isinstance(low, float) or isinstance(high, float) else 'int'
    }]

    iqa_metric, metric_direction = ops_Pipeline.initialise_iqa(args_dict['iqaMethod'])

    def run_tests(params):
        new_value = params[hex_address]
        try:
            local_file, hex_new, iqa_score = ops_Pipeline.img_pipeline(device, args_dict, tune_dict, new_value,
                                                                       iqa_metric)

            # Build output directory names
            output_dir = '{}\\{}'.format(args_dict['output_dir'], tune_dict['address'])
            ext = args_dict['remoteOutputExt']

            # Create output path if it doesn't exist
            Path(output_dir).mkdir(parents=True, exist_ok=True)

            # Move file so results are easier to view
            shutil.move(str(local_file), '{}\\{}_{}.{}'.format(output_dir, iqa_score, new_value, ext))

            resultsArray.append([tune_dict['name'], tune_dict['address'], new_value, hex_new, iqa_score, local_file])

            return {'iqa_score': iqa_score}

        except Exception:
            return Exception

    # Run the optimization
    best_params, best_score, _foo, _bar = optimize(
        experiment_name="test",
        objective_name="iqa_score",
        evaluation_function=run_tests,
        parameters=search_space,
        minimize=bool(metric_direction),
        total_trials=120,
    )

    # render(plot_contour(model=test, param_x='x1', param_y='x2', metric_name='hartmann6'))
    # Return the best parameter value and corresponding score
    return best_params[hex_address], best_score[0]['iqa_score']


def run_optimisation(device, args_dict, lib_dict):
    for tuneDict in lib_dict:
        hex_address = tuneDict['address']
        hex_name = tuneDict['name']
        best_param, best_score = optimize_one_param(device, args_dict, tuneDict, hex_address)
        for result in resultsArray:
            print(result)
        print(f"Best value for {hex_address} {hex_name}: {best_param}, Score: {best_score}")
