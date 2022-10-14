# GCam-Autotune
Using Frida to patch GCam libs live in RAM, retrieve photo and assess result

# Working:

RAM patcher

Lib value generator

Reading from Rivov API for values

Memory monitor (sort of, see below)

# Currently developing

Keep memory monitor running until photo has processed

OpenCV code to crop target image out of main image for assessment

Image assessment code


# To-do:

Write possible value ranges to lib value JSON array so Ax knows what an acceptable value is

Merge code to pull new photo from device

Write Ax experiment taking lib values as args


# Requirements:

Ubuntu (version?)

OpenCV with CUDA compiled (https://github.com/rsnk96/Ubuntu-Setup-Scripts)

