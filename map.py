# maps have two parameters: functions and tuples-lists-objects
# Data of n tuples will be used as parameter of a function f(x) with one parameter
# i.e. the function values of the dataset a_1,a_2,...a_n will be calculated,
# then maps are useful to get as an object f(a_1), f(a_2), f(a_3), ..., f(a_n)

import math
def area(x):
    """Area of circle"""
    return math.pi*x**2
radii=[1,2,3,4,math.pi]
mapp=map(area,radii)
print(type(mapp))
# maps can be converted to lists
print(list(mapp))

##################################################
temperatures=[('Berlin',29),('Cairo',34),('Buenos Aires', 29), ("Los angeles", 26),
              ("Tokyo", 22), ("New York", 27), ("London", 17), ("Beijing",25), ("Athens", 38)]
celcius_to_fahrenheit=lambda data:(data[0],(9/5)*data[1]+32)
print(list(map(celcius_to_fahrenheit,temperatures)))


