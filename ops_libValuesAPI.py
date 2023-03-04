import json
import os
import urllib.request
import struct


def get_value_ranges(armtype, hexlength):
    # As we only need to calculate to and from a hex value and not an actual decimal etc, we just need a integer
    # value in hex. The AI optimisation program simply requires a range to tune. We then convert that to hex and
    # Patch into instruction.

    match armtype.lower():
        # These instructions we overwrite with a simple fmov
        case 'armrpl' | 'arm' | 'armorr':
            low = -31
            high = 31
            return [low, high]
        # These instructions always contain a #0xbbbb value so we fix their value to 4
        case 'armflt' | 'armfltmovk' | 'armdbl' | 'armdec':
            low = int('0' * 4, 16)
            high = int('f' * 4, 16)
            return [low, high]
        # Doubles are a fixed length integer
        case 'dbl':
            low = int('0' * hexlength, 16)
            high = int('f' * hexlength, 16)
            return [low, high]
        # Floats we need to convert to decimal as we can't support float resolution
        case 'flt':
            low = struct.unpack("<d", struct.pack("<d", float.fromhex('0' * hexlength)))[0]
            high = struct.unpack("<d", struct.pack("<d", float.fromhex('f' * hexlength)))[0]
            return [low, high]
        case _:
            return 'invalid'


def get_lib_values():
    # File paths for previously saved parameters
    params_path = 'libParams.json'
    bad_params_path = 'libBadParams.json'

    # Big thanks to Sergei Rivov for his exceptional API!
    req_url = 'http://152.67.78.6:8080/v2/addresses/by_version/?lib_version=8.4.400_rc19&allow_in_testing=true'

    # Check if file exists first so we don't smash Rivovs' API
    if os.path.isfile(params_path):
        f = open(params_path)
        lib_params = json.load(f)
    else:
        # File doesn't exist so call online API
        with urllib.request.urlopen(req_url) as req:
            lib_params = json.load(req)

    # Sanitize item lists for items we can't handle automatically
    bad_types = ["HEXSTRING", "ARMMANUAL"]
    bad_params = []

    # Loop through tunable dictionary
    for tunable in lib_params.copy():
        # Loop through known bad types
        for substring in bad_types:
            if tunable.get('arm_type').find(substring) != -1:
                # Write bad ones out so we can save them later
                print(tunable)
                bad_params.append(tunable)
                # Then we can remove them from the dictionary
                lib_params.remove(tunable)

    # Add additional fields we need for the auto-tune to work
    for tunable in lib_params:
        tune_range = get_value_ranges(tunable.get('arm_type'), len(tunable.get('hex_original')))
        tunable['range'] = [tune_range[0], tune_range[1]]

    # Sort dict by address as that's the most likely way they're called without relying on MemoryAccessMonitor
    # MemoryAccessMonitor hasn't been confirmed working at this stage
    lib_params.sort(key=lambda x: x["address"])

    # Write values we CAN change automatically out to file so we don't smash Rivovs' API
    with open(params_path, "w") as outfile:
        write_params = json.dumps(lib_params, ensure_ascii=True, indent=2)
        outfile.write(write_params)

    # Write values we CAN'T change automatically so these can be manually split and/or fixed
    # Note that this writes in append mode - it's so it doesn't overwrite if there's no values in subsequent passes!
    if bad_params:
        with open(bad_params_path, "a") as outfile:
            write_params = json.dumps(bad_params, ensure_ascii=True, indent=2)
            outfile.write(write_params)

    return lib_params


# If you want to generate the files themselves just delete the JSONs then uncomment and run

get_lib_values()
