# thx ChatGPT lul

# To use the ax-platform Python package to perform Bayesian 
# optimization for your black box function score=optimise(x), 
# where x is a randomly selected value from the range 
# specified in the range key in your JSON dict, you can follow
# these steps:

# Import the necessary libraries:

import json
import random
import numpy as np
from ax import optimize

#Load the JSON dict and extract the range for each parameter:
with open('path_to_json_file.json') as f:
    data = json.load(f)

# Extract ranges for each parameter
parameter_ranges = {}
for d in data:
    parameter_ranges[d['name']] = (d['range'][0], d['range'][1])

# Define the black box function score=optimise(x) that takes in a dictionary of parameter values and returns the score:

def optimise(params):
    # Do something with the parameter values to calculate score
    x = params['Zipper1']
    y = params['Coef spatial']
    score = x * y  # Change this to your actual black box function
    return {'score': score}

# Define the search space using the parameter ranges:

search_space = []
for name, (lower, upper) in parameter_ranges.items():
    search_space.append({
        'name': name,
        'type': 'range',
        'bounds': [lower, upper],
        'value_type': 'float' if isinstance(lower, float) or isinstance(upper, float) else 'int'
    })

# Run the Bayesian optimization using the optimize() function from the ax package:

best_parameters, best_score = optimize(
    parameters=search_space,
    evaluation_function=optimise,
    minimize=True,
    total_trials=100
)

# The optimize() function takes in the search space, the black box function, and other parameters such as whether to minimize or maximize the score 
# (minimize=True in this case), and the total number of trials to run (total_trials=100 in this case). The function returns the best set of parameters 
# and the corresponding best score found during the optimization.

# Note that you will need to modify the black box function optimise(params) to actually perform the optimization for your specific use case, 
# but the general steps outlined above should provide a good starting point.
