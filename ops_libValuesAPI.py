import json
import os
import urllib.request
import struct
import ops_FridaPatcher

def get_value_ranges(armType,hexLength):
    
    # As we only need to calculate to and from a hex value and not an actual decimal etc, we just need a integer value in hex.
    # The AI optimisation program simply requires a range to tune. We then convert that to hex and patch into instruction.
    
    match armType.lower():
        # These instructions we overwrite with a simple fmov
        case 'armrpl' | 'arm' | 'armorr':
            low = -31
            high = 31
            return [low, high]
        # These instructions always contain a #0xbbbb value so we fix their value to 4
        case 'armflt' | 'armfltmovk' | 'armdbl' | 'armdec':
            low = int('0' * 4,16)
            high = int('f' * 4,16)
            return [low, high]
        # Doubles are a fixed length integer
        case 'dbl':
            low = int('0' * hexLength,16)
            high = int('f' * hexLength,16)
            return [low, high]
        # Floats we need to convert to decimal as we can't support float resolution
        case 'flt':
            low = struct.unpack("<d", struct.pack("<d", float.fromhex('0' * hexLength)))[0]
            high = struct.unpack("<d", struct.pack("<d", float.fromhex('f' * hexLength)))[0]
            return [low, high]
        case _:
            return 'invalid'

def get_lib_values():
    # File paths for previously saved parameters
    paramsPath = 'libParams.json'
    badParamsPath = 'libBadParams.json'

    # Big thanks to Sergei Rivov for his exceptional API!
    reqUrl = 'http://152.67.78.6:8080/v2/addresses/by_version/?lib_version=8.4.400_rc19&allow_in_testing=false'

    # Check if file exists first so we don't smash Rivovs' API
    if os.path.isfile(paramsPath):
        f = open(paramsPath)
        libParams = json.load(f)
    else:
        # File doesn't exist so call online API
        with urllib.request.urlopen(reqUrl) as req:
            libParams = json.load(req)

    # Sanitize item lists for items we can't handle automatically
    badTypes = ["HEXSTRING", "ARMMANUAL"]
    badParams = []

    # Loop through tunable dictionary
    for tunable in libParams.copy():
        # Loop through known bad types
        for substring in badTypes:
            if tunable.get('arm_type').find(substring) != -1:
                # Write bad ones out so we can save them later
                print(tunable)
                badParams.append(tunable)
                # Then we can remove them from the dictionary
                libParams.remove(tunable)
                
    # Add additional fields we need for the auto-tune to work
    for tunable in libParams:
        tuneRange = get_value_ranges(tunable.get('arm_type'),len(tunable.get('hex_original')))
        tunable['range'] = [tuneRange[0],tuneRange[1]]

    # Sort dict by address as that's the most likely way they're called without relying on MemoryAccessMonitor
    # MemoryAccessMonitor hasn't been confirmed working at this stage
    libParams.sort(key=lambda x: x["address"])

    # Write values we CAN change automatically out to file so we don't smash Rivovs' API
    with open(paramsPath, "w") as outfile:
        writeParams = json.dumps(libParams, ensure_ascii=True , indent=2)
        outfile.write(writeParams)
        
    # Write values we CAN'T change automatically so these can be manually split and/or fixed
    # Note that this writes in append mode - it's so it doesn't overwrite if there's no values in subsequent passes!
    if badParams:
        with open(badParamsPath, "a") as outfile:
            writeParams = json.dumps(badParams, ensure_ascii=True , indent=2)
            outfile.write(writeParams)
        
    return libParams