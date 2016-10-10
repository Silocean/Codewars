'''
Description:

Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21
C# RomanDecode.Solution("XXI") -- should return 21

Courtesy of rosettacode.org
'''
def solution(roman):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i, x in enumerate(roman):
        tmp = i + 1
        if tmp == len(roman):
            sum += d[x]
        else:
            if d[x] < d[roman[tmp]]:
                sum += (-1) * d[x]
            else:
                sum += d[x]
    return sum