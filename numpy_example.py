# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jay Ahlschwede
#               Aidan Murphy
#               Israel Prado
#               Bobby Hao
# Section:      525
# Assignment:   lab 12
# Date:         11/18/2022
## As a team, we have gone through all required sections of the # tutorial, and each team member understands the material
#
# YOUR CODE HERE
import numpy as n

A=[[0,1,2,3],
   [4,5,6,7],
   [8,9,10,11]]

B=[[0,1],
   [2,3],
   [4,5],
   [6,7]]

C=[[0,1,2],
   [3,4,5]]

A=n.array(A)
B=n.array(B)
C=n.array(C)

D=A@B@C
D=n.array(D)

DT=D.transpose()#move row to col, col to row

E=n.sqrt(D)/2

print(f'A={A}\n\nB={B}\n\nC={C}\n\n')

print(f'D={D}\n\n')

print(f'D^T={DT}\n\n')

print(f'E={E}\n\n')