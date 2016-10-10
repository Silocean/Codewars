'''
Description:

Scientists working internationally use metric units almost exclusively. Unless that is, they wish to crash multimillion dollars worth of equipment on Mars.

Your task is to write a simple function that takes a number of meters, and outputs it using metric prefixes.

In practice, meters are only measured in "mm" (thousandths of a meter), "cm" (hundredths of a meter), "m" (meters) and "km" (kilometers, or clicks for the US military).

For this exercise we just want units bigger than a meter, from meters up to yottameters, excluding decameters and hectometers.

All values passed in will be positive integers. e.g.

meters(5);
// returns "5m"

meters(51500);
// returns "51.5km"

meters(5000000);
// returns "5Mm"
See http://en.wikipedia.org/wiki/SI_prefix for a full list of prefixes
'''
import math
def meters(x):
    rank = int(math.log10(x)) / 3
    symbol = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']
    return "{0:g}{1}m".format(float(x) / 1000 ** rank, symbol[rank])