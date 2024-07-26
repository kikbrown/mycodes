# 40. Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
import math 


def distance_points(x1, x2, y1, y2):
    a = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    return a



x=int(float(input('Enter x1: ')))
t=int(float(input('Enter x2: ')))
y=int(float(input('Enter y1: ')))
z=int(float(input('Enter y2: ')))
print(distance_points(x, t, y, z))