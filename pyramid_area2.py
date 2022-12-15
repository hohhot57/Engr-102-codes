# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jay Ahlschwede
#               Israel Prado
#               Bobby Hao
#               Aidan Murphy
# Section:      525
# Assignment:   6.11.2: LAB: Pyramid area
# Date:         04 10 2022

#import math
from math import *
#asks user input for the side
side_length = float(input("Enter the side length in meters: "))
#asks user input for layers
num_layer = int((input("Enter the number of layers: ")))
#area for the top triangle
top_tri = 3 * side_length * side_length 
#area for the bottom ones
bot_tri = 3 * side_length * (num_layer * side_length)
#area for the faces of the bottom triangles
bot_face = ((num_layer * side_length)**2) * (sqrt(3)/4)
#total area
tot_area = (top_tri + bot_tri)/2 * num_layer + bot_face
#output
print("You need {:.2f} m^2 of gold foil to cover the pyramid".format(tot_area))

    