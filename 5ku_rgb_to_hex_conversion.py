'''
Description:

The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range should be rounded to the closest valid value.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''
def rgb(r, g, b):
    #your code here :)
    if r>255:
        r = 'FF'
    elif r<0:
        r = '00'
    else:
        r = hex(r)[2:].zfill(2).upper()
    if g>255:
        g = 'FF'
    elif g<0:
        g = '00'
    else:
        g = hex(g)[2:].zfill(2).upper()
    if b>255:
        b = 'FF'
    elif b<0:
        b = '00'
    else:
        b = hex(b)[2:].zfill(2).upper()
    return r+g+b