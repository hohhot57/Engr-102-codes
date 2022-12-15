# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jay Ahlschwede
#               Bobby Hao
#               Israel Prado
#               Aidan Murphy
# Section:      525
# Assignment:   4.15 Lab Boolean
# Date:         21 9 2022
#
#
# YOUR CODE HERE


A=input('Enter True or False for a: ')
B=input('Enter True or False for b: ')
C=input('Enter True or False for c: ')

############ Part A ############
if A=="True" or A=="T" or A=="t":
    A = True
elif A=="False" or A=="F" or A=="f":
    A = False
else:
    A = "Input is not permissible"
    
if B=="True" or B=="T" or B=="t":
    B = True
elif B=="False" or B=="F" or B=="f":
    B = False
else:
    B = "Input is not permissible"
    
if C=="True" or C=="T" or C=="t":
    C = True
elif C=="False" or C=="F" or C=="f":
    C = False
else:
    C = "Input is not permissible"
############ Part B ############
combo= A and B and C
combo_or= A or B or C
print("a and b and c:", combo)
print("a or b or c:", combo_or)

############ Part C ############
switch= (B and not(A)) or (A and not(B))

print("XOR:",switch)

ot= (A and B and C) or (A and not(B or C)) or (B and not(A or C)) or (C and not(B or A))
print("Odd number:", ot)
