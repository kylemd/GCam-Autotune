import frida
import time
import libValuesAPI
import json
import sys

# Define message handler for Frida JS so script can communicate.
def msg_handler(message , payload): 
	print(message)
	print(payload)

def run_memory_monitor(package_name):
		
	libdict = libValuesAPI.GetLibValues()										#Call Rivov API for values

	# Connect to device and spawn packagem
	device = frida.get_usb_device()
	pid = device.spawn([package_name])
	device.resume(pid)
	time.sleep(3) 																#Without waiting Java.perform silently fails
	session = device.attach(pid)

	script = session.create_script(open('fridaMemoryMonitor.js').read())
	script.on("message" , msg_handler) 											#Calls message handler for JS
	script.load()

	#Loop through values and pass them to the memory monitor
	script.exports.monitorlibmemory(json.dumps(libdict))
	termInput = input()