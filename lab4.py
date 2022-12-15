# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Aidan Murphy
#               Jay Ahlschwede
#               Israel Prado
#               Bobby Hao
# Section:      ENGR-102-525
# Assignment:   Lab Topic 4 team
# Date:         16/09/2022

from math import *

print("How much did you pay?")
pay = float(input())

print("How much did it cost?")
cost = float(input())

change = pay - cost

if (change > 0):
    print(f"you received {change} in change. That is...")
    
else:
    print("you received nothing in change")