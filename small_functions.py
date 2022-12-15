# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 9
# Date:         11/02/2022
from math import *
import math
from math import pi
def parta(radius_sphere,radius_hole):
    # v of cap = 1/3 * pi * (3R-h)h^2, h is the height of the sphere
   # a = 0.5 * radius_sphere * math.sqrt(3) *2
  #  h = math.sqrt(3) * a
  #  vol_hole = pi * (radius_hole **2) * a
    #vol_sphere_cap = (1/3 * pi) * (3 * radius_sphere - h ) * (h**2)
    
   # radius = radius_sphere
   # h = radius - 1/4*radius_hole*pi*2
   # v = 2* ((pi * h ** 2)/3) * (3*radius-h)
   # return v
 #   vol_bead = 4/3 * pi * radius_sphere **3 - vol_hole #method 1
    rs= radius_sphere
    rh=radius_hole
    b = sqrt(rs**2-rh**2)#length of the cylinder
    h = rs - b#height of the cap
    vcaps = 2* (((pi * h ** 2)/3) * 3*rs - h *((pi * h ** 2)/3))#volume of the cap using the formula from WIKI
    vcylinder = pi * rh**2 * 2 * b
    vtot = 4/3*pi*rs**3 - vcaps - vcylinder#v total is the volume of spehere - vcaps - vcylinder
    return vtot

'''Write a function named partb that will take in as a parameter a positive integer 𝑛 and 
determines if 𝑛 can be calculated as the sum of 2 or more consecutive positive, odd integers. If 
it can, return a list of the numbers, otherwise return False. '''

def partb(n):
    p = 1
    list = []
    
    if n%4 == 2:#sum of 2 consectutive numbers cant get 2 when divided by 4 
        return False
    f = False#f is the flag
    while not f:
        q = p - 1 
        while q >= 0:#make sure q is greater than 0 and start the while loop. stops when it's false
            if ((p*p)-(q*q))== n:#if the sum of the two of the pos and odd intgers equal to n
                for y in range (q+1,p+1):
                    list.append((2*y)-1)#make sure the number is odd and append it
                f = True#stop the loop
                break
            q -= 1
        p +=1
    if len(list)==1:
        return False
    return list
    

'''Write a function named partc that will take in as parameters a single character, a person’s
name, company, and email, and returns a single string of the person’s digital business card. Use
the character as a border, and provide 2 spaces as padding on either side of the longest entry.
Your function must return a single string, do NOT print the digital card.
'''
def partc(single_char, person_name,company,email):
    
    
    
    chars = single_char * 26#tried to print out the example output
    string_name = single_char.ljust(15)+" "+person_name+" "*(22-len(person_name))+" "+single_char#left justed the leftmost column of the char and tried to print out the other required stuff
    string_company = single_char.ljust(15)+" "+company+" "*(22-len(company)) + " "+single_char
    string_email = single_char.ljust(15)+" "+email+" "*(22-len(email)) +" "+ single_char
    all_strings = chars.ljust(30)+"\n" +str(string_name).center(20,' ') + "\n"+str(string_company).center(15,' ')+"\n"+str(string_email).center(10,' ') +"\n"+chars
    #all_strings = (f'{chars}') + "\n" + 
    return all_strings

def partd(list):
    minnum = min(list)#built in function for finding the minimum of a list
    maxnum = max(list)#built in function for finding the maxmum of a list
    median = int(sum(list)/len(list))#fomula for find the median of a list 

    return(minnum,median,maxnum)

'''Write a function named parte that takes in as parameters two parallel lists: a list of times (in 
increasing order), and a list of distances traveled by that point in time. The function should 
return a new list giving the velocity between consecutive time measurements. The new list 
should have a length of one less than the original lists. '''

    

def parte(times,distances):#2lists
    vel=[]
    for i in range(len(times)-1):#list of times in increasing order
        p= (distances[i+1] - distances[i])/(times[i+1] - times[i])#find the velocity 
        vel.append(p)#update the velocity
    return vel

'''Write a function named partf that takes in as a parameter one list of numbers and determines if 
two of the numbers in the list add to 2026. If they do, return the product of the two numbers, 
otherwise return False. '''

def partf(list):
  #  l = int([list])
    for i in list:#any number in the list 
        for j in list:#another number in the list
            if i + j == 2026:#if the sum of the i and j equal to 2026 return the product of i and j
                return (i * j)

    
    return False#else, returns false
