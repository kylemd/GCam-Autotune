# GCam-Autotune
Using Frida to patch GCam libs live in RAM, retrieve photo and assess result

# Working:

RAM patcher
Lib value generator
Reading from Rivov API for values

# Currently developing

Monitor memory with Frida to determine order that lib values are accessed - having an odd file not found error trying to load the js?

# To-do:

Write possible value ranges to lib value JSON array so Ax knows what an acceptable value is

Merge code to pull new photo from device

OpenCV code to crop target image out of main image for assessment

Finalise and push image assessment code

Write Ax experiment taking lib values as args
