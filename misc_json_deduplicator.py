import ops_libValuesAPI as LibAPI

lib_dict = LibAPI.get_lib_values()

for i in lib_dict:
    print(i['address'])
    for j in lib_dict:
        if i['address'] == j['address'] and i['id'] is not j['id']:
            print("ID {} is duplicate of ID {}. {} {}".format(i['id'], j['id'], i['address'], i['name']))
