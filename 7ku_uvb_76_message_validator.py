'''
Description:

In Russia, there is an army-purposed station named UVB-76 or "Buzzer" (see also https://en.wikipedia.org/wiki/UVB-76). Most of time specific "buzz" noise is being broadcasted, but on very rare occasions, the buzzer signal is interrupted and a voice transmission in Russian takes place. Transmitted messages have always the same format like this:

MDZHB 01 213 SKIF 38 87 23 95

or:

MDZHB 80 516 GANOMATIT 21 23 86 25

Message format consists of following parts:

Initial keyword "MDZHB";
Two groups of digits, 2 digits in first and 3 in second ones;
Some keyword of arbitrary length consisting only of uppercase letters;
Final 4 groups of digits with 2 digits in each group.
Your task is to write a function that can validate the correct UVB-76 message. Function should return "True" if message is in correct format and "False" otherwise.
'''
def validate(message):
  # Good luck!
  import re
  return bool(re.match(r'^MDZHB \d{2} \d{3} [A-Z]* \d{2} \d{2} \d{2} \d{2}$', message))