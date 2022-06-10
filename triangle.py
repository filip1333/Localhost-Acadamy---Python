# Create function that takes 3 floats as parameters na returns True of False
# True if u can build triangle with straight angle with these lenghts
import math


def is_rectangular_triangle(a, b, c):
    list_angle = sorted([a, b, c])
    return math.pow(list_angle[0], 2) + math.pow(list_angle[1], 2) == math.pow(list_angle[2], 2)


is_rectangular_triangle(0.15, 0.2, 0.25)
is_rectangular_triangle(5.4, 3.1, 6.7)
'''
def is_rectangular_triangle(a, b, c):
    list_angle = sorted([a, b, c])
    return math.pow(list_angle[0], 2) + math.pow(list_angle[1], 2) == math.pow(list_angle[2], 2)
a = float(input('Enter first side in float: '))
b = float(input('Enter second side in float: '))
c = float(input('Enter third side in float: '))
is_rectangular_triangle(a, b, c)
'''
