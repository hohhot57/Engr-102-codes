# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 6.15.1
# Date:         10/02/2022
import math

#ask for user input
n = int(input("Enter a value for n:"))


firstsum = (n*(n-1))//2#equation for finding the sum of first n-1 terms
secondsum = 0#counter

r = 1#count the numbers of n sum up to firstsum

#loop starts n+1 and it runs untils secondsum is less than firstsum
while(secondsum < firstsum):
    secondsum += n + r 

    r += 1
#if secondsum is the same as the first sum then it's a balanced number
if(secondsum == firstsum):
    print( n,'is a balancing number with r =',r-1)
#if they are not the same then it's not a balanced number
else:
    print( n,'is not a balancing number')
