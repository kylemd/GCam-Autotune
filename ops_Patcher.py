import frida
import binascii
from ProjectPepega import arm as hex2arm


# Define a message handler so Python can communicate with the remote Frida instance.
def msg_handler(message, payload):
    print(message)
    print(payload)


# Javascript defaults to Big Endian so the bits in the libpatcher value appear backwards.
# It's much easier to fix it here than in JavapatchScript.
def swap_endianness(hex_value):
    ba = bytearray.fromhex(hex_value)
    ba.reverse()
    return ba.hex()


# Function to start the remote Frida instance
def load_hook(package_name):
    # Connect to device and spawn package
    device = frida.get_usb_device()

    pid = None
    for a in device.enumerate_applications():
        if a.identifier == package_name:
            pid = a.pid
            break

    session = device.attach(pid)

    # Method to cleanly connect and spawn app
    # Connect to device and spawn package (cleanly)
    # device = frida.get_usb_device()
    # pid = device.spawn([package_name])
    # device.resume(pid)

    # #Without waiting Java.perform silently fails
    # time.sleep(1)

    # session = device.attach(pid)

    # Create a new JS rampatcher script from string.
    patch_script = session.create_script("""
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

    patch_script.on('message', msg_handler)  # Calls message handler for JS
    patch_script.load()

    return patch_script


# Patch lib in RAM with Frida
def patch_ram(patchscript, tunedict, newvalue):
    # #Loop through and Patch for each tunable item in the API
    # for tunable in libParams:
    hex_address = tunedict['address']
    hex_original = tunedict['hex_original']
    hex_size = tunedict['length_in_lib']

    hex_value = hex2arm.generate_hex(hex_original, newvalue)
    if hex_value is None:
        hex_value = hex(int(newvalue))
    else:
        hex_value = swap_endianness(hex_value.upper())

    patchscript.exports.libpatcher(hex_address, hex_value, hex_size)

    return hex_value


# Patch lib file on device using remote Python instance
def patch_file(device, libpath, tunedict, newvalue):
    # Loop through and Patch for each tunable item in the API
    # for tunable in libParams:
    hex_original = tunedict['hex_original']
    hex_size = int(tunedict['length_in_lib'])

    hex_value = hex2arm.generate_hex(hex_original, newvalue)
    if hex_value is None:
        hex_value = hex(int(newvalue))

    dec_address = int(tunedict['address'], 16)
    if len(hex_value) % 2 != 0:
        hex_value = '0' + hex_value

    shell_value = binascii.unhexlify(hex_value)

    if len(shell_value) < len(hex_value) // 2:
        padding_length = len(hex_value) // 2 - len(shell_value)
        shell_value = b'\x00' * padding_length + shell_value

    patch_cmd = "printf '{}' | dd of={} bs=1 seek={} count={} conv=notrunc".format(
        shell_value, libpath, dec_address, hex_size)

    device.shell(patch_cmd)

    return hex_value
