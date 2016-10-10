'''
Description:

Write function getNumberFromString which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
'''
def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))