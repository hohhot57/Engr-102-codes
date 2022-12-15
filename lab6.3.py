import math

n = int(print("Enter a value for n:"))


sumpre_n = (n*(n-1))//2

#variable
sumpost_n = 0

r = 1

while(sumpost_n < sumpre_n):
    sumpost_n += n + r 
    r += 1

if(sumpost_n == sumpre_n):
    print('%d is a balancing number with r = %d'%(n,r-1))

else:
    print('%d is not a balancing number'%(n))
