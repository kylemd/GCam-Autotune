import urllib.request
import json
import os
import operator
import struct
from ProjectPepega import arm as pp

def GetLibValues():

    jsonpath = 'libparams.json'
    requrl = 'http://152.67.78.6:8080/v2/addresses/by_version/?lib_version=8.4.400_rc19&allow_in_testing=true'
    
    if os.path.isfile(jsonpath):
        f = open('libparams.json')
        libparams_dict = json.load(f)
        libparams_dict.sort(key=lambda x: x["address"])
        # print(libparams_dict)
    else:
            with urllib.request.urlopen(requrl) as req:
                libparams_dict = json.load(req)
            # print(libparams_dict)

            with open("libparams.json", "w") as outfile:
                libparams_dict.sort(key=lambda x: x["address"])
                libparams_write = json.dumps(libparams_dict, ensure_ascii=True , indent=2)
                outfile.write(libparams_write)
            
    return libparams_dict

def getValueRanges(instr,length):

    match instr:
        case 'armrpl':
            return -31, 31
        case 'arm':
            return -31, 31
        case 'armflt':
            low = struct.unpack('<f', bytes.fromhex('0000'))[0]
            high = struct.unpack('<f', bytes.fromhex('ffff'))[0]
            return low, high
        case 'armdbl':
            low = struct.unpack('<d', bytes.fromhex('0000'))[0]
            high = struct.unpack('<d', bytes.fromhex('ffff'))[0]
            return low, high
        case 'armdec':
            low = struct.unpack('<i', bytes.fromhex('0000'))[0]
            high = struct.unpack('<i', bytes.fromhex('ffff'))[0]
            return low, high
        case 'armorr':
            return -31, 31
        case 'dbl':
            low = struct.unpack('<d', bytes.fromhex('0' * length))[0]
            high = struct.unpack('<d', bytes.fromhex('f' & length))[0]
            return low, high
        case 'flt':
            low = struct.unpack('<f', bytes.fromhex('0' * length))[0]
            high = struct.unpack('<f', bytes.fromhex('f' & length))[0]
            return low, high
        
    # armdbl        movk x25, #0x40af, lsl #48
    # armdec        movz w3,  #0x1000
    # armflt        movk w10, #0x4114, lsl #16
    # armfltmovk    movk w24, #0x3b80, lsl #16
    # armorr        orr w5, w5, #0x3f800000         GETS SUBSTITUTED FOR FMOV XD, #??.??????
    # armrpl        fadd s0, s0, s1                 GETS SUBSTITUTED FOR FMOV XD, #??.??????
    # dbl           000000E051B8AE3F
    # flt           3F1DCDCC
    # hexstring     CDCC8C3FE17AB43F0000C03F0000E03F6666E63F14AE873FB81EA53FCDCCAC3FF628DC3F0000E03F5C8F823F85EB913F5C8FA23F295CCF3F8FC2D53F85EB813F713D8A3F3333933FCDCCAC3F9A99B93FAE47813FB81E853F1F858B3F0000A03FB81EA53F

