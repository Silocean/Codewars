'''
Description:

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior") 

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")
'''
def to_camel_case(text):
    #your code here
    text = text.replace('_', '-')
    return ''.join(x.capitalize() if i>0 else x for i, x in enumerate(text.split('-')))