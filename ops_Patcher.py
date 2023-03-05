import frida
from ProjectPepega import arm as hex2arm


# Patch lib file on device using in-built Linux GNU tools
def patch_file(device, libpath, tunedict, newvalue):
    hex_original = tunedict['hex_original']
    hex_size = int(tunedict['length_in_lib'])

    hex_value = hex2arm.generate_hex(hex_original, newvalue)
    if hex_value is None:
        hex_value = hex(int(newvalue))

    dec_address = int(tunedict['address'], 16)

    patch_cmd = "echo '{}' | xxd -r -p | dd of={} bs=1 seek={} count={} conv=notrunc".format(
        hex_value, libpath, dec_address, hex_size)

    device.shell(['su', '-c', patch_cmd])

    return hex_value
