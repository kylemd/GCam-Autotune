# thx ChatGPT lul

# Yes, you can blacklist parts of a range if the black box 
# function returns an error or returns 0 using the reject_fn 
# argument in the search_space definition. 
# The reject_fn is a function that takes in a set of parameter
# values and returns True if the corresponding run should be 
# rejected.

# Here's an example of how you can modify the code to 
# blacklist parts of the range if the black box function 
# returns an error or returns 0:

import json
from ax import optimize



# Load the JSON dict
with open('path_to_json_file.json') as f:
    data = json.load(f)

# Define the search space and black box function for one parameter
def optimize_one_parameter(parameter_name):
    parameter_data = next(d for d in data if d['name'] == parameter_name)
    search_space = [{
        'name': parameter_name,
        'type': 'range',
        'bounds': [parameter_data['range'][0], parameter_data['range'][1]],
        'value_type': 'float' if isinstance(parameter_data['range'][0], float) or isinstance(parameter_data['range'][1], float) else 'int',
        'reject_fn': lambda p: optimise(p[parameter_name]) == 0 or optimise(p[parameter_name]) is None
    }]

    def black_box_function(params):
        x = params[parameter_name]
        score = optimise(x)  # Call your actual black box function with the current parameter value
        return {'score': score}

    # Run the optimization
    best_parameters, best_score = optimize(
        parameters=search_space,
        evaluation_function=black_box_function,
        minimize=True,
        total_trials=100
    )

    # Return the best parameter value and corresponding score
    return best_parameters[parameter_name], best_score['score']

# In the search_space definition, we've added a reject_fn that checks whether the black box function returns 0 or None for the current parameter value. If it does, the corresponding run will be rejected and the range will be blacklisted.

# You can call this function for each parameter in your JSON dict to optimize each one individually:

for d in data:
    parameter_name = d['name']
    best_parameter, best_score = optimize_one_parameter(parameter_name)
    print(f"Best value for {parameter_name}: {best_parameter}, Score: {best_score}")

# Note that in the black_box_function, we're calling your actual black box function optimise(x) with the current parameter value. You will need to modify this to call your own black box function with the current parameter value for your specific use case.