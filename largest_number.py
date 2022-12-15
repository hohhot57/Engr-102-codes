# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 4.13
# Date:         09/21/2022

x = float(input("Enter number 1: "))#asks for user input
y = float(input("Enter number 2: "))
z = float(input("Enter number 3: "))

if(x > y and x > z):#if x is larger than y, and z prints x
    print("The largest number is",x)
elif(y > x and y > z):
    print("The largest number is",y)
else:
    print("The largest number is",z)

