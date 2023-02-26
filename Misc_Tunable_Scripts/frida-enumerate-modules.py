# Small module to print out all modules loaded by app.
# This is useful when the cam you're using has renamed libgcastartup.so
# So patching fails (as it can't find it)
# e.g. Shamim using external lib uses libpatched_jni.so 

import sys
import frida

package_name = 'com.shamim.cam'

def on_message(message, data):
	print("[%s] -> %s" % (message, data))

def main(package_name):
	# Connect to device and spawn package
	device = frida.get_usb_device()

	pid = None
	for a in device.enumerate_applications():
		if a.identifier == package_name:
			pid = a.pid
			break

	session = device.attach(pid)

	script = session.create_script("""
		Process.enumerateModules({
			onMatch: function(module){
				console.log('Module name: ' + module.name + " - " + "Base Address: " + module.base.toString());
			}, 
			onComplete: function(){}
		});
""")

	script.on('message', on_message)
	script.load()
	input('[!] Press <Enter> at any time to detach from instrumented program.\n\n')
	session.detach()

if __name__ == '__main__':

	main(package_name)