'''
Description:

Given 2 strings, your job is to find out if there is a substring that appears in both strings. You will return true if you find a substring that appears in both strings, or false if you do not. We only care about substrings that are longer than one letter long.

Examples:

*Example 1*
SubstringTest("Something","Fun"); //Returns false

*Example 2*
SubstringTest("Something","Home"); //Returns true
In the above example, example 2 returns true because both of the inputs contain the substring "me". (soMEthing and hoME)
In example 1, the method will return false because something and fun contain no common substrings. (We do not count the 'n' as a substring in this Kata because it is only 1 character long)

Rules:

Lowercase and uppercase letters are the same. So 'A' == 'a'.
We only count substrings that are > 1 in length.

Input:

Two strings with both lower and upper cases.

Output:

A boolean value determining if there is a common substing between the two inputs.
'''
def substring_test(str1, str2):
    #your code here
    str1 = str1.lower()
    str2 = str2.lower()
    for x in range(len(str1)-1):
        if str1[x:x+2] in str2:
            return True
    else:
        return False