import urllib.request
import json
import os

def GetLibValues():

    jsonpath = 'libparams.json'
    requrl = 'http://152.67.78.6:8080/v2/addresses/by_version/?lib_version=8.4.400_rc19&allow_in_testing=true'
    
    if os.path.isfile(jsonpath):
        f = open('libparams.json')
        libparams_dict = json.dumps(json.load(f))
    else:
        try:
            with urllib.request.urlopen(requrl) as req:
                libparams_dict = json.dumps(json.load(req))

            with open("libparams.json", "w") as outfile:
                outfile.write(libparams_dict)
                
        except req.exceptions.RequestException as e:
            print(e)
            exit()
        except (req.exceptions.InvalidJSONError, TypeError):
            print("Invalid JSON Error.")
            exit()
            
    return libparams_dict