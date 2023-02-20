from bayes_opt import BayesianOptimization
import pipeline
import ops_libValuesAPI as libapi

def OptimizeGCam(lower,upper):
    """Function with unknown internals we wish to maximize.

    This is just serving as an example, for all intents and
    purposes think of the internals of this function, i.e.: the process
    which generates its output values, as unknown.
    """
    package = 'com.shamim.cam'
    activity = "com.android.camera.CameraLauncher"
    output_dir = '/sdcard/DCIM/Camera'
    output_format = 'jpg'

    score = pipeline.pipeline(device,package,activity,hexaddress,hexoriginal,newvalue)
    return (1000 - score)

libparams = libapi.get_lib_values()

for i in libparams:
    print(i['range'])
    # optimizer = BayesianOptimization(
    #     f=OptimizeGCam,
    #     pbounds=i['range'],
    #     verbose=2, # verbose = 1 prints only when a maximum is observed, verbose = 0 is silent
    #     random_state=1,
    # )

    # optimizer.maximize(
    #     init_points=1,
    #     n_iter=20,
    # )

    # print(optimizer.max)