
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER Lab 1.11
# Date:         08/26/2022
#
#
# YOUR CODE HERE

#from math import sin

#Part 1: 
#For t = 25 minutes, the position p = 9026.0 kilometers 
#Part 2: 

#For t = 300 minutes, the position p = 10219.078642554414 kilometers 
from math import *


T1=10 #first time
T2=T1+45 #second time
D1=2026 #distance at T1
D2=23026 #distance at T2
Ti=25

print("For t = 25 minutes, the position p =",((D2-D1)/(T2-T1))*(Ti-T1)+D1, "kilometers")


