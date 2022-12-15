#
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jay Ahlschwede
#               Israel Prado
#               Bobby Hao
#               Aidan Murphy
# Section:      525
# Assignment:   LAB4.14
# Date:         9 21 2022
#
A=int(input("Please enter the coefficient A: "))
B=int(input("Please enter the coefficient B: "))
C=int(input("Please enter the coefficient C: "))

Ax=A

Bx=B
#The A part of Quadratic equation 
if (A<0 and A!=-1): #Fixed
    A='-' + str(abs(A)) + "x^2"
elif (A==1):
    A="x^2 "
elif (A==-1):
    A="- x^2 "
elif (A==0):
    A=""
else:
    A=str(abs(A))+"x^2 "
#The B part of Quadratic equation

if (B<0 and B!=-1):
    B="- " + str (abs(B)) + "x"
elif (Ax!=0) and (B==1):
    B="+ x"
elif (Ax==0) and (B==1):
    B="x"
elif (B==-1):
    B="- x"
elif (B==0):
    B=""
else:
    if (Ax==0):
        B=str (B) + "x"
    else:
        B="+" + str (B) + "x"
        
        

if (C<0 and Bx!=0):
    C="- "+str(abs(C))
elif(C<0 and Bx==0):
    C="- "+str(abs(C))
elif (C==1):
    C=" + 1"
elif (C==0):
    C=""
else:
    C=" + "+ str(abs(C))
    
print("The quadratic equation is {}{}{} = 0".format(A,B,C))