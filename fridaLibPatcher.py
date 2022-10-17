import frida
from frida_tools import pull as fp
import time
from ProjectPepega import arm as hex2arm

# Instructions:
# Install magisk-frida and adb on a rooted phone
# Change package name to camera being used
# Make sure libpatcher is disabled!

# Define message handler for Frida JS so script can communicate.
def msgHandler(message , payload): 
	print(message)
	print(payload)

def patchAndSnap(addr_hex, orig_hex, new_value):
	# Camera package name. Change this if needed
	packageName = 'org.codeaurora.snapcam'

	# Connect to device and spawn package
	device = frida.get_usb_device()
	pid = device.spawn([packageName])
	device.resume(pid)
	time.sleep(1) 														#Without waiting Java.perform silently fails
	session = device.attach(pid)

	script = session.create_script(open("fridaLibPatcher.js").read())
	script.on("message" , msgHandler) 									#Calls message handler for JS
	script.load()
	device.resume(pid)

	#Loop through and patch values in RAM
	for i in addr_hex:
		new_hex = hex2arm.generate_hex(orig_hex[i], new_value[i])
		script.exports.libpatcher(addr_hex[i], new_hex)
	
	#Take a photo and pull photo from device
	# script.exports.getphotoname()