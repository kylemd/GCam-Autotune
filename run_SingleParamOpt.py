import json
import ops_libValuesAPI as libapi
import pipeline
from ax import optimize

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
        x = params[hex_tunable]
        t = d
        score = pipeline.test(t,x)  # Call your actual black box function with the current parameter value
        return {'score': score}

    # Run the optimization
    best_parameters, best_score = optimize(
        parameters=search_space,
        evaluation_function=RunPatchTests,
        minimize=True,
        total_trials=5,
        objective_name='score'
    )

    # Return the best parameter value and corresponding score
    return best_parameters[hex_tunable], best_score['score']

# Load the JSON dict
data = libapi.get_lib_values()

for d in data:
    hex_tunable = d['address']
    best_parameter, best_score = OptimizeSingleParam(hex_tunable)
    print(f"Best value for {hex_tunable}: {best_parameter}, Score: {best_score}")