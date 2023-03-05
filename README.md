# GCam-Autotune

Auto tuner for finding the optimum values for Google Camera lib tunables.

# How does it work?

We iteratively test the effects that changing each parameter has on image quality.

We use Facebooks' ax-platform package for Bayesian optimisation to try and find the optimum value in as few tests as 
possible - we don't want to be running 100,000s of experiments on each value as it would take forever!

# Does it work?

This is a very experimental - it is my first Python project so expect bugs!

I upload everything I do so people can collaborate and I can learn. Don't be shy - fork, modify, test, post issues etc.

# Requirements

A **Google Camera mod** installed.

**Root** on the handset you want to test.

**Python 3.10.8** and git installed.

**Pytorch** set up on your machine

**PyCharm** or **VS Code** (recommended, not needed - helps with debugging and reporting issues)

# How to use

I recommend using `pyenv` to install the required Python version.

Use `git clone` to get this repository onto your hard drive and open it up in PyCharm.

Once you've done that, run `pip install -r requirements.txt` in the project root to install all dependencies.

Go into `AutoTuner.py` and make sure the values in args_dict are correct. If you want to run the tests proper, remove
the `testParam` field - this is only one tunable that I'm using for debugging currently.


# To-do:

More robust exception catching

Correctly read user variables from JSON

De-duplicate the values in Rivovs' API

Write code to roll-back changes to lib if that tunable isn't working