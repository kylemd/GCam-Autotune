import struct
import itertools
import json

sabre_luma = "9A99993F159A99193E1DAE50223F0A0F0DCDCC8C3F15CDCCCC3D1D95806D3E0A0F0D9A99993F150AD7A33D1D09997A3E0A0F0DCDCC8C3F158FC2F53D1D0E06743E0A0A0D0000803F1D68CEB13E12050D0000A0400A570A0F0D9A99993F159A99193E1D14FA003F0A0F0D0000803F15CDCCCC3D1D49CCBD3E0A0F0D0000803F15CDCCCC3D1D37E0A43E0A0F0D3333333F15295C0F3E1D7B0A023F0A0A0DCDCCCC3D1DD1FF143F12050D0000A0410A570A0F0D9A99993F15CDCC4C3E1D1093243F0A0F0D3333333F15CDCCCC3D1DD08A203F0A0F0D836FCD3E15CDCCCC3D1D54EEF13E0A0F0DE0790E3F15CDCCCC3D1D93D7B93E0A0A0D9142C23E1DAF3C9F3D"

def from_hex_to_float(hex_string: str) -> str:
    """
    :param hex_string: hex string to convert to float
    :return: float
    """
    return struct.unpack("<f", bytes.fromhex(hex_string))[0]

def alternating_size_chunks(iterable, steps):
    n = 0
    i = 0
    id = 2323 #Current as of 2023/02/16
    base_address = 0x00AFCBC3
    step = itertools.cycle(steps)
    data = []

    while n < len(iterable):
        next_step = next(step)
        address = base_address + n
        hexvalue = iterable[n:n + next_step]

        if len(hexvalue) == 8:
            data.append({
                "id": str(id),
                "name": "Wavelet Luma [" + str(i) + "]",
                "lib_version": "8.4.400_rc19",
                "arm_type": "FLT",
                "disasm": "HEX VALUE",
                "added_on": "",
                "is_in_testing": "false",
                "description": "Wavelet luma denoise",
                "address": '00' + hex(address)[2:].upper(),
                "length_in_lib": len(hexvalue),
                "hex_original": hexvalue,
                "extracted_value": from_hex_to_float(hexvalue),
                "added_by": ""
            })
            i = i + 1
            id = id + 1

        n += next_step

    return data

extracted_floats = alternating_size_chunks(sabre_luma, ((8, 2, 8, 2, 8, 6) * 4 + (8, 2, 8, 24)) * 3)

with open('wavelet_luma.json', "w") as outfile:
        writeParams = json.dumps(extracted_floats, ensure_ascii=True , indent=2)
        outfile.write(writeParams)