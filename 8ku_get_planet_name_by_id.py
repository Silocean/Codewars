'''
Description:

The function is not returning the correct values. Can you figure out why?
'''
def get_planet_name(id):
    # This doesn't work; Fix it!
    return {
        1:"Mercury",
        2:"Venus",
        3:"Earth",
        4:"Mars",
        5:"Jupiter",
        6:"Saturn",
        7:"Uranus", 
        8:"Neptune",
        }.get(id)