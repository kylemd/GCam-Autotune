import urllib.request
import json
import operator

def GetLibValues(operation,libvalues):

    requrl = 'http://152.67.78.6:8080/v2/addresses/by_version/?lib_version=8.4.400_rc19&allow_in_testing=true'

    if libvalues == 'textfile':
        f = open('libparams.json')
        libparams_dict = json.load(f)
    else:
        try:
            with urllib.request.urlopen(requrl) as req:
                libparams_dict = json.load(req)
            libparams_dict.sort(key=operator.itemgetter('address'))

            libparams_obj = json.dumps(libparams_dict, indent=2)

            with open("libparams.json", "w") as outfile:
                outfile.write(libparams_obj)
        except req.exceptions.RequestException as e:
            print(e)
            exit()
        except (req.exceptions.InvalidJSONError, TypeError):
            print("Invalid JSON Error.")
            exit()

    answer = []
    
    for return_dict in libparams_dict:
        if operation == 'patcher':
            answer.append([return_dict['address'],return_dict['hex_original']])
        elif operation == 'monitor':
            answer.append([return_dict['address'],return_dict['length_in_lib']])
        else:
            print('Invalid option entered, return lib value types are patcher or monitor')
            
    return answer