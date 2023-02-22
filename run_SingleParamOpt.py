import json
import ops_libValuesAPI as libapi
import pipeline
from ax import optimize

# Load the JSON dict
data = libapi.get_lib_values()

# Define the search space and black box function for one parameter
def optimize_one_parameter(parameter_name):
    parameter_data = next(d for d in data if d['address'] == parameter_name)
    search_space = [{
        'name': parameter_name,
        'type': 'range',
        'bounds': [parameter_data['range'][0], parameter_data['range'][1]],
        'value_type': 'float' if isinstance(parameter_data['range'][0], float) or isinstance(parameter_data['range'][1], float) else 'int',
    }]

    def black_box_function(params):
        x = params[parameter_name]
        tunable = d
        score = pipeline.generate(tunable,x)  # Call your actual black box function with the current parameter value
        return {'score': score}

    # Run the optimization
    best_parameters, best_score = optimize(
        parameters=search_space,
        evaluation_function=black_box_function,
        minimize=True,
        total_trials=20
    )

    # Return the best parameter value and corresponding score
    return best_parameters[parameter_name], best_score['score']

for d in data:
    parameter_name = d['address']
    best_parameter, best_score = optimize_one_parameter(parameter_name)
    print(f"Best value for {parameter_name}: {best_parameter}, Score: {best_score}")