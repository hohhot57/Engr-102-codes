# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jay Ahlschwede
#               Israel Prado
#               Bobby Hao
#               Aidan Murphy
# Section:      525
# Assignment:   6.11.1: LAB: Pyramid area
# Date:         04 10 2022
#

import math
from math import *
#defining the function to calculate the area
def area_cover():
    #user inputs
    side_length = float(input("Enter the side length in meters: "))
    num_layer= int(input("Enter the number of layers: "))
    area = 0
    
    for i in range(num_layer):
        n = i + 1
        area += 3 * n * side_length**2 + (sqrt(3)/4)*(n*side_length)**2 - (sqrt(3)/4) * (i*side_length)**2#equation for surface area
    return area#return the area of the pyramid
#call the function
area = area_cover()

#output
print("You need {:.2f} m^2 of gold foil to cover the pyramid".format(area))