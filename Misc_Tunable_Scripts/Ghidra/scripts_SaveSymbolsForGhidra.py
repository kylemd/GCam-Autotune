import ops_libValuesAPI
import os

ghidraDir = os.getcwd() + '\\output\\_ghidra\\'
ghidraFile = 'ghidraLibTunables.json'

#Make new folder for the output file

if not os.path.exists(ghidraDir):
    os.mkdir(ghidraDir)
    
# Get the lib tunables from Rivovs' API making sure to keep non-auto tunables.
libParams = ops_libValuesAPI.get_lib_values()
ghidraText = []

# Append a string for ImportSymbolsScript.py in Ghidra to an array
for tunable in libParams:
    s = str(tunable['name'])
    s = ''.join(s.split())
    
    if s == "":
        s = "UNKNOWN"
    else:
        s.replace(" ", "_")
    
    ghidraText.append(
        str(s + ' 0x' + tunable['address'] + ' l')
    )

path = os.path.join(ghidraDir, ghidraFile)

with open(path, "w") as outfile:
    for line in ghidraText:
        outfile.write(line + '\n')