# Small module to print out all modules loaded by app.
# This is useful when the cam you're using has renamed libgcastartup.so
# So patching fails (as it can't find it)
# e.g. Shamim using external lib uses libpatched_jni.so 

import sys
import frida
import time
import adbutils

package_name = 'com.androidcamera.ucvm'
messages = []

def on_message(message, data):
	messages.append(message['payload'])

def main(package_name):
	# Connect to device and spawn package
	adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
	d = adb.device()
	
	device = frida.get_usb_device(3)
	pid = device.spawn([package_name])
	device.resume(pid)

	#Without waiting Java.perform silently fails
	time.sleep(1)

	session = device.attach(pid)

	time.sleep(3)

	script = session.create_script("""
		const lib = Process.findModuleByName("libgcastartup.so");
		console.log(`!!! Loaded ${lib.name} @ ${lib.base}. Saving exports to file.\n`);
		lib.enumerateExports().forEach(sym=>{send(`${sym.name},${sym.address}`)})
	""")

	script.on('message', on_message)
	script.load()

	with open('lib_exports.txt', "w") as outfile:
		outfile.write('\n'.join(messages))
		
	session.detach()

if __name__ == '__main__':

	main(package_name)

		# 	({
		# 	onMatch: function(module){
		# 		console.log('Module name: ' + module.name + " - " + "Base Address: " + module.base.toString());
		# 	}, 
		# 	onComplete: function(){}
		# });