# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 6.14.1
# Date:         10/02/2022

import math
from math import *
n=int(input("Enter a positive integer:"))
#Given a number n, if n is even then the next number is the floor of the square root of n. 
#If n is odd, then the next number is the floor of n^3/2. The Juggler sequence ends when 
#n reaches 1.
print("The Juggler sequence starting at", n, "is:")
count=0#counter
while n>1:#start of the while loop 
  print(n, end=', ')
  if n%2==0:#floor of square root of n
      n=int(sqrt(n))
      count+=1
  elif n%2>0:#floor of n^3/2
        n=int(n**(3/2))
        count+=1
print("1")
print("It took", count, "iterations to reach 1")