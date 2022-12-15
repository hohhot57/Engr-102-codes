# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 4.18.1
# Date:         09/21/2022

#asks for user input

days = int(input("Please enter a positive value for day: "))

if (days < 0):#if the input is smaller than 0, warn the user
    print("You entered an invalid number!")
else:
    gadgets = 0#initialize gadgets to 0

    if (days <= 10):#calculate the amt of gadgets when <= 10 days
        gadgets = 5 * days
    #end_tendays = 0 + (first_tendays * x)
    elif (days > 10 and days <= 60):#calculate the amt of gadgets when > 10 and <= 60 days
        gadgets = 50 + 50 * (days-10)

    elif(days >= 60 and days <= 101):#calculate the amt of gadgets when >= 60 and <= 101 days
  
         n = days - 60
         gadgets = 2550 + ((50 * n) - ((n*(n+1))//2)) # total gadgets
    else:
         gadgets = 3720 + 10



print(f'The total number of gadgets produced on day {days} is {gadgets}')


