

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      YOUR SECTION NUMBER
# Assignment:   THE ASSIGNMENT NUMBER Lab 2.8
# Date:         08/31/2022
#
#
# YOUR CODE HERE
from math import*
T1=10 #first time
T2=T1+45 #second time
D1=2026 #distance at T1
D2=23026 #distance at T2
Ti=25
print("Part 1:")
print("For t = 25 minutes, the position p =",((D2-D1)/(T2-T1))*(Ti-T1)+D1, "kilometers")#doing the calculation following the equation
print("Part 2:")
ISS=((D2-D1)/(T2-T1))*(Ti-T1)+D1

#circumference of circle
radius=6745 #radius the ISS orbits
Circum=2*pi*radius
#Linear Interpolation
TP=300
ISS=((D2-D1)/(T2-T1))*(TP-T1)+D1
print("For t = 300 minutes, the position p =",(ISS % Circum), "kilometers")#doing the calculation following the equation


