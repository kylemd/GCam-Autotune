apivalues = ['id', 'name', 'lib_version', 'arm_type',
                'disasm', 'added_on', 'is_in_testing', 'address', 'description',
                'length_in_lib','hex_original','extracted_value','added_by']

print('Arguments:\n')
print('textfile: loads libparams.json from root dir\n')
print('Enter following arguments to return values from dictionary:\n')
for x in apivalues:
    print(x, end = ', ')
print('\n')