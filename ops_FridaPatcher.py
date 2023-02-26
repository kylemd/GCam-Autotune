import frida
import time
from ProjectPepega import arm as hex2arm

#Define a message handler so Python can communicate with the remote Frida instance.
def msg_handler(message, payload):
    print(message)
    print(payload)

# Javascript defaults to Big Endian so the bits in the libpatcher value appear backwards. 
# It's much easier to fix it here than in JavapatchScript.
def swap_endianness(hexstring):
	ba = bytearray.fromhex(hexstring)
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

def PatchRAM(patchScript,tunable,newvalue):
    # #Loop through and patch for each tunable item in the API
	# for tunable in libParams:
	hexAddress = tunable['address']
	hexOriginal = tunable['hex_original']
	hexSize = tunable['length_in_lib']
	hexName = tunable['name']

	hexNew = hex2arm.generate_hex(hexOriginal, newvalue)
	if hexNew == None:
		hexNew = hex(int(newvalue))
	else:
		hexNew = swap_endianness(hexNew.upper())

	#print('Patching {} {} with {} {}'.format(hexName,hexAddress,hexNew,newvalue))
	#Execute the hook
	patchScript.exports.libpatcher(hexAddress, hexNew, hexSize)

	return hexNew
  
# def generate_and_write(patchScript, libParam, newValue):
# 	for tunable in libParam:
# 		hexAddress = tunable['address']
# 		hexOriginal = tunable['hex_original']
# 		hexSize = tunable['length_in_lib']
# 		hexName = tunable['name']

# 		print('Patching ' + hexName + ', address ' + hexAddress)
# 		hexNew = hex2arm.hex_to_hex(hexOriginal, newValue)

# 		patchScript.exports.libpatcher(hexAddress, hexNew, hexSize)
  
		
    # single tunable item
    # if newValue is hex
    # for n in range(0xffff):
	