import struct
from ProjectPepega import arm as pp

def getValues(type: str,limit: str, chars: int):
    if limit == "low":
        hex = '0000' + ('0' * chars)
    elif limit == 'high':
        hex = 'ffff' + ('f' * chars)
    else:
        return
    
    print(hex)
    numval = struct.unpack(type, bytes.fromhex(hex))[0]
    
    return numval 

value_limits = [['armrpl',-31,31],
                ['arm',-31,31],
                ['armflt',getValues('<f','low',4),getValues('<f','high',4)],
                ['armdbl',getValues('<d','low',8),getValues('<d','high',8)],
                ['armdec',getValues('<i','low',4),getValues('<i','high',4)],
                ['armorr',getValues('<d','low',8),getValues('<d','high',8)]]

for x in value_limits:
    print(value_limits[x][0][0])
    
# armdbl        movk x25, #0x40af, lsl #48
# armdec        movz w3,  #0x1000
# armflt        movk w10, #0x4114, lsl #16
# armfltmovk    movk w24, #0x3b80, lsl #16
# armorr        orr w5, w5, #0x3f800000
# armrpl        fadd s0, s0, s1
# dbl           000000E051B8AE3F
# flt           3F1DCDCC
# hexstring     CDCC8C3FE17AB43F0000C03F0000E03F6666E63F14AE873FB81EA53FCDCCAC3FF628DC3F0000E03F5C8F823F85EB913F5C8FA23F295CCF3F8FC2D53F85EB813F713D8A3F3333933FCDCCAC3F9A99B93FAE47813FB81E853F1F858B3F0000A03FB81EA53F

