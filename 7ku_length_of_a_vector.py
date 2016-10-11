'''
Description:

For a given 2D vector described by cartesian coordinates of its initial point and terminal point in the following format: [[x1, y1], [x2, y2]], your function must return this vector's length presented as a float.

Error must be less than 0.0000001 * result.

Coordinates can be integers or floats.
'''
def vector_length(vector):
    import math
    return math.sqrt((vector[0][0]-vector[1][0]) ** 2 + (vector[0][1]-vector[1][1]) ** 2)