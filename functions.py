# functions
import math
def f():
    pass
f()
def ping():
    return "Ping!"
print(ping())

def volume(r):
    return 4/3*math.pi*r**3

print(volume(2))

def triangle_area(b,h):
    return 0.5*b*h
print(triangle_area(2,3))

def cm(feet=0,inches=0):
    """ Converts a length from inches and feet to cms"""
    inches_to_cm=inches*2.54
    feet_to_cm=feet*12*2.54
    return inches_to_cm+feet_to_cm
print(cm(feet=2))
print(cm(inches=3))
print(cm(feet=2,inches=3))
print(cm())