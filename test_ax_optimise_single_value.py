# thx ChatGPT lul

# If you want to run the optimize() function on one item from
# the dict at a time, you can modify the search space and 
# black box function accordingly. 
# Here's an example of how you can modify the code to 
# optimize one parameter at a time:






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
        'value_type': 'float' if isinstance(parameter_data['range'][0], float) or isinstance(parameter_data['range'][1], float) else 'int'
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

# You can call this function for each parameter in your JSON dict to optimize each one individually:




for d in data:
    parameter_name = d['name']
    best_parameter, best_score = optimize_one_parameter(parameter_name)
    print(f"Best value for {parameter_name}: {best_parameter}, Score: {best_score}")

# Note that in the black_box_function, we're calling your actual black box function optimise(x) with the current parameter value. 
# You will need to modify this to call your own black box function with the current parameter value for your specific use case.
