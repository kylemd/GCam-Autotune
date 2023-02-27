import shutil

from pathlib import Path
from ax import optimize

import ops_libValuesAPI as lib_api
import ops_ADB as ctrl
import ops_Pipeline

resultsArray = []

# Define the search space and black box function for one parameter
def optimize_one_param(device,argsDict,tuneDict,hexAddress):
    tunableData = next(d for d in tuneDict if d['address'] == hexAddress)
    low = tunableData['range'][0]
    high = tunableData['range'][1]

    searchSpace = [{
        'name': hexAddress,
        'type': 'range',
        'bounds': [low, high],
        'value_type': 'float' if isinstance(low, float) or isinstance(high, float) else 'int'
    }]

    iqaMetric,metricDirection = ops_Pipeline.initialise_iqa(argsDict['iqaMethod'])

    def run_tests(params):
        newValue = params[hexAddress]
        try:
            localFile, hexNew, iqaScore = ops_Pipeline.img_pipeline(device,argsDict,tuneDict,newValue,iqaMetric)

            # Build output directory names
            outputDir = '{}\\{}'.format(argsDict['outputDir'],tuneDict['address'])
            ext = argsDict['remoteOutputExt']

            # Create output path if it doesn't exist
            Path(outputDir).mkdir(parents=True, exist_ok=True)

            #Move file so results are easier to view
            shutil.move(str(localFile),'{}\\{}_{}_{}.{}'.format(outputDir,iqaScore,newValue,ext))


            resultsArray.append([tuneDict['name'],tuneDict['address'],newValue,hexNew,iqaScore,localFile])

            return {'iqa_score': iqaScore }
        
        except Exception:
            return Exception
        
    # Run the optimization
    bestParams, bestScore, _foo, _bar  = optimize(
        experiment_name="test",
        objective_name="iqa_score",
        evaluation_function=run_tests,
        parameters=searchSpace,
        minimize=bool(metricDirection),
        total_trials=120,
    )

    # render(plot_contour(model=test, param_x='x1', param_y='x2', metric_name='hartmann6'))
    # Return the best parameter value and corresponding score
    return bestParams[hexAddress], bestScore[0]['iqa_score']

def run_optimisation(device,argsDict,libDict):
    for tuneDict in libDict:
        hexAddress = tuneDict['address']
        hexName = tuneDict['name']
        bestParam, bestScore = optimize_one_param(device,argsDict,tuneDict,hexAddress)
        for result in resultsArray:
            print(result)
        print(f"Best value for {hexAddress} {hexName}: {bestParam}, Score: {bestScore}")
