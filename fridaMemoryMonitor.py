import frida
import time
import sys
import libValuesAPI
import json

# Define message handler for Frida JS so script can communicate.
def msgHandler(message , payload): 
	print(message)
	print(payload)

libdict = libValuesAPI.GetLibValues()										#Call Rivov API for values

# Camera package name. Change this if needed
packageName = 'org.codeaurora.snapcam'

# Connect to device and spawn package
device = frida.get_usb_device()
pid = device.spawn([packageName])
device.resume(pid)
time.sleep(1) 																#Without waiting Java.perform silently fails
session = device.attach(pid)

script = session.create_script(open('fridaMemoryMonitor.js').read())
script.on("message" , msgHandler) 											#Calls message handler for JS
script.load()

#Loop through values and pass them to the memory monitor
script.exports.monitorlibmemory(json.dumps(libdict))