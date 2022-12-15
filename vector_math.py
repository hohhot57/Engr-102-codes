# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 7.26.1
# Date:         10/11/2022


from math import *
#do calculation for vector values
def magcal():
    a = sqrt(sum([A[i] * A[i] for i in range(len(A))]))
    b = sqrt(sum([B[i] * B[i] for i in range(len(B))]))
    print("The magnitude of vector A is {:.5f}".format(a))
    print("The magnitude of vector B is {:.5f}".format(b))
#A+B
def a_and_b():   

    print(f"A + B is {[float(A[i] + B[i]) for i in range(len(A))]}")
#A-B
def a_minus_b():
    print(f"A - B is {[float(A[i] - B[i]) for i in range(len(A))]}")
#dot products
def dotpro():
    print(f"The dot product is { sum([A[i] * B[i] for i in range(len(A))]):.2f}")
#user inputs
A = (str(input("Enter the elements for vector A:"))).split(" ")
B = (str(input("Enter the elements for vector B:"))).split(" ")

# evaluate arbitrary expressions from a string-based input
if A !=0:
    A = [eval(i) for i in A]
if B !=0:
    B = [eval(i) for i in B]
print()
#call the output functions
magcal()
a_and_b()
a_minus_b()
dotpro()


