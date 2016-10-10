'''
Description:

Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules. In this kata, you are a mischevious hacker that has set out to sabatoge all his good code.

Your job is to take PEP8 compatible function names and convert them to camelCase. For example:

zebulansNightmare('camel_case') == 'camelCase'
zebulansNightmare('zebulans_nightmare') == 'zebulansNightmare'
zebulansNightmare('get_string') == 'getString'
zebulansNightmare('convert_to_uppercase') == 'convertToUppercase'
zebulansNightmare('main') == 'main'
'''
def zebulansNightmare(name):
    s = name.replace('_', ' ').title().replace(' ', '')
    return s[0].lower()+s[1:]