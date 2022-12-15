# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 5.4
# Date:         09/27/2022

from math import *
import math
#user input 
excesstemp=float(input("Enter the excess temperature:"))
#paramter for excess temp(range of the points)
slopeab=float((log10(7000/1000)/log10(5/1.3)))      
slopebc=float((log10((1.5*10**6)/7000)/log10(30/5)))
slopecd=float((log10((2.5*10**4)/(1.5*10**6))/log10(120/30)))
slopede=float((log10((1.5*10**6)/(2.5*10**4))/log10(1200/120)))
if excesstemp<1.3: #point a begins at 1.3 but will not be available 
  print("Surface heat flux is not available")
if excesstemp>=1.3 and excesstemp<5:#point b start at 1.3 and ends at 5
  heat1=1000*(((excesstemp)/1.3)**slopeab)
  print("The surface heat flux is approximately{:.0f} W/m^2" .format(heat1))
if excesstemp >= 5 and excesstemp <30:#point c start at 5 and ends at 30
  heat2=7000*(((excesstemp)/5)**slopebc)
  print("The surface heat flux is approximately{:.0f} W/m^2".format ( heat2))
if excesstemp>=30 and excesstemp<120:#point d start at 30 and ends at 120
  heat3=(1.5*10**6)*(((excesstemp)/30)**slopecd)
  print("The surface heat flux is approximately{:.0f} W/m^2 ".format( heat3))
if excesstemp>=120 and excesstemp<1200:#point e start at 120 and ends at 1200
  heat4=(2.5*10**4)*(((excesstemp)/120)**slopede)
  print("The surface heat flux is approximately{:.0f} W/m^2".format( heat4))
if excesstemp>1200: #if the value is > 1200, error.
  print("Surface heat flux is not available")