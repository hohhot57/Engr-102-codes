# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 6.13
# Date:         09/21/2022


'''Write a program named howdy_whoop.py that takes as input from the user two positive integers. 
Output the numbers 1 to 100, each on its own line, unless the number is evenly divisible by one or both 
of the integers entered by the user. If the number is evenly divisible by the first integer, print Howdy. If 
it’s evenly divisible by the second integer, print Whoop. If it’s evenly divisible by both, print Howdy 
Whoop. Format your output as shown below. User input is shown in bold and red text. '''
#asks for user inputs
n1 = int(input("Enter an integer:"))
n2 = int(input("Enter another integer:"))
#counter
count = 1
#for the numbers in range 1 to 100
for count in range(1,101):
  #if they are both evenly disvisable 
    if count % n2 ==0 and count % n1 ==0:
        print("Howdy Whoop")
#if only divisable by n1
    elif count % n1 == 0:
        print("Howdy")
#if only divisable by n2
    elif count % n2 == 0:
        print("Whoop")
#if odd, print the number
    
    else:
        print(count)
    count += 1

