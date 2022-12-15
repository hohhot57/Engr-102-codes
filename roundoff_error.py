# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 4.17
# Date:         09/21/2022

############ Part A ############
#from re import A
from math import sqrt

a  = 1/7
print(f'a = {a}')
b = a*7
print(f'b = a * 7 = {b}')#if no roundoff, it shouldn be 1

c = 2 * a
d = 5 * a 
f = c + d
print(f'f = 2 * a + 5 * a = {f}')#if no roundoff, it shouldn be 1

x = sqrt(1 / 3)
print(f'x = {x}')
y = x * x * 3
print(f'y = x * x * 3 = {y}')
z = x * 3 * x
print(f'z = x * 3 * x = {z}')#the value is not 1

############ Part B ############

TOL = 1e-10
# check if b and f a re equal within specified tolerance
if abs(b -f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print(f'b and f are NOT euqal within tolerance of {TOL}')

if abs(y - z) < TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print(f'y and z are NOT euqal within tolerance of {TOL}')

############ Part C ############

m = 0.1
print(f'm = {m}')
n = 3 * m
print(f'n = 3 * m = 0.3 {n==0.3}')
p = 7 * m
print(f'p = 7 * m = 0.7 {p==0.7}')
q = n + p
print(f'q = n + p = 1 {q==1}')

