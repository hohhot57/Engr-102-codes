
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 2.10
# Date:         09/07/2022
#
#
# YOUR CODE HERE

 #1) linearly interpolate between (t0, x0) and 
#(t2, x2) for t1 with x1 as the result; 2) repeat for (t0, y0) and (t2, y2) for t1 with y1 as the result; 3) repeat 
#for (t0, z0) and (t2, z2) for t1 with z1 as the result. The result will be (x1, y1, z1) associated with time t1. 

#At time 12 seconds, observed position was (8, 6, 7) meters 
#• At time 85 seconds, observed position was (-5, 30, 9) meters 
# You want to find the position at time 30 seconds 
from math import *

X0=8#x distance at t0
Y0=6#y distance at t0
Z0=7#z distance at t0

X2=-5#x distance at t2
Y2=30#y distance at t2
Z2=9#z distance at t2

T0=12 #first time
T2=85 #third time
T1=30

print("At time 30.0 seconds:")
print("x1 = ", ((X2-X0)/(T2-T0))*(T1-T0)+X0, "m")# finding x1, y1, and z1
print("y1 = ", ((Y2-Y0)/(T2-T0))*(T1-T0)+Y0, "m")
print("z1 = ", ((Z2-Z0)/(T2-T0))*(T1-T0)+Z0, "m")
print("-----------------------")
T4=37.5
print("At time 37.5 seconds:")
print("x2 = ", ((X2-X0)/(T2-T0))*(T4-T0)+X0, "m")
print("y2 = ", ((Y2-Y0)/(T2-T0))*(T4-T0)+Y0, "m")
print("z2 = ", ((Z2-Z0)/(T2-T0))*(T4-T0)+Z0, "m")
print("-----------------------")
T5=45
print("At time 45.0 seconds:")
print("x3 = ", ((X2-X0)/(T2-T0))*(T5-T0)+X0, "m")
print("y3 = ", ((Y2-Y0)/(T2-T0))*(T5-T0)+Y0, "m")
print("z3 = ", ((Z2-Z0)/(T2-T0))*(T5-T0)+Z0, "m")
print("-----------------------")
T6=52.5
print("At time 52.5 seconds:")
print("x4 = ", ((X2-X0)/(T2-T0))*(T6-T0)+X0, "m")
print("y4 = ", ((Y2-Y0)/(T2-T0))*(T6-T0)+Y0, "m")
print("z4 = ", ((Z2-Z0)/(T2-T0))*(T6-T0)+Z0, "m")
print("-----------------------")#printing ----------------
T7=60
print("At time 60.0 seconds:")
print("x5 = ", ((X2-X0)/(T2-T0))*(T7-T0)+X0, "m")
print("y5 = ", ((Y2-Y0)/(T2-T0))*(T7-T0)+Y0, "m")
print("z5 = ", ((Z2-Z0)/(T2-T0))*(T7-T0)+Z0, "m")
#print("-----------------------")
