import math

def sphere_volume(radius):
    vol = (4/3) * math.pi * pow(radius, 3)
    return vol

print(sphere_volume(3))