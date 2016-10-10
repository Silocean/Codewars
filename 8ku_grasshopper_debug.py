'''
Description:

Debug celsius converter

Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. Unfortunately his code has some bugs.

Find the errors in the code to get the celsius converter working properly.

To convert fahrenheit to celsius:

celsius = (fahrenheit - 32) * (5/9)
'''
def weather_info (temp):
    c = convertToCelsius(temp)
    if c < 0:
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convertToCelsius(fahrenheit):
  celsius = (fahrenheit - 32) * (5/9.0)
  return celsius