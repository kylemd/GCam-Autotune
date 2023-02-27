import frida
from ProjectPepega import arm as hex2arm

#Define a message handler so Python can communicate with the remote Frida instance.
def msg_handler(message, payload):
    print(message)
    print(payload)

# Javascript defaults to Big Endian so the bits in the libpatcher value appear backwards. 
# It's much easier to fix it here than in JavapatchScript.
def swap_endianness(hexValue):
	ba = bytearray.fromhex(hexValue)
	ba.reverse()
	return ba.hex()

# Function to start the remote Frida instance
def load_hook(packageName):

	# Connect to device and spawn package
	device = frida.get_usb_device()

	pid = None
	for a in device.enumerate_applications():
		if a.identifier == packageName:
			pid = a.pid
			break

	session = device.attach(pid)

	# Connect to device and spawn package (cleanly)
	# device = frida.get_usb_device()
	# pid = device.spawn([packageName])
	# device.resume(pid)

	# #Without waiting Java.perform silently fails
	# time.sleep(1)
														
	# session = device.attach(pid)

	# Create a new JS rampatcher script from string.
	patchScript = session.create_script("""
			function writemem(libOffset,newHex,sizeHex) {
				const libRamAddress = Process.findModuleByName("libpatched_jni.so");
				const ramOffset = new NativePointer(libRamAddress.base.add("0x" + libOffset));
				const patchedHex = Number('0x' + newHex);
				const sizeInBytes = Number(sizeHex);

				Memory.patchCode(ramOffset,sizeInBytes,code => {
					const writer = new Arm64Writer(code, ramOffset);
					writer.putInstruction(patchedHex);
					writer.flush();
				});
			}

			rpc.exports = {
						libpatcher: writemem
			};
	""")

	patchScript.on('message',msg_handler) 									#Calls message handler for JS
	patchScript.load()
 
	return patchScript

# Patch lib in RAM with Frida
def patch_ram(patchScript,tuneDict,newValue):
    # #Loop through and patch for each tunable item in the API
	# for tunable in libParams:
	hexAddress = tuneDict['address']
	hexOriginal = tuneDict['hex_original']
	hexSize = tuneDict['length_in_lib']
	hexName = tuneDict['name']

	hexValue = hex2arm.generate_hex(hexOriginal, newValue)
	if hexValue == None:
		hexValue = hex(int(newValue))
	else:
		hexValue = swap_endianness(hexValue.upper())

	#print('Patching {} {} with {} {}'.format(hexName,hexAddress,hexNew,newvalue))
	#Execute the hook
	patchScript.exports.libpatcher(hexAddress, hexValue, hexSize)

	return hexValue

# Patch lib file on device using remote Python instance
def patch_file(device,libPath,tuneDict,newValue):
    # #Loop through and patch for each tunable item in the API
	# for tunable in libParams:
	hexAddress = tuneDict['address']
	hexOriginal = tuneDict['hex_original']
	hexSize = tuneDict['length_in_lib']
	hexName = tuneDict['name']

	hexValue = hex2arm.generate_hex(hexOriginal, newValue)
	if hexValue == None:
		hexValue = hex(int(newValue))
	else:
		hexValue = swap_endianness(hexValue.upper())

	device.shell(["python","/sdcard/autotune_patcher.py",libPath,hexAddress,hexValue])

	return hexValue