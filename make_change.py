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
# Assignment:  
# Date:         9 13 2022
#
pay=float(input("How much did you pay? "))
price=float(input("How much did it cost? "))
change=pay-price

print(f'You received ${change:.2f} in change. That is...')

if(change!=0): #to make the different amounts of change
    quarters=change//.25
    aq=change%.25
    dimes=aq//.10
    ad=aq%.10
    nickels=ad//.05
    an=ad%.05
    pennies=round(an/.01)

if quarters==1:
    print("1 quarter")
if quarters>1:
    print(f'{quarters:.0f} quarters')
    
if dimes==1:
    print("1 dime")
if dimes>=1:
    print(f'{dimes:.0f} dimes')
    
if nickels==1:
    print("1 nickel")
if nickels>1:
    print(f'{nickels:.0f} nickels')
    
if pennies==1:
    print("1 penny")
if pennies>1:
    print(f'{pennies:.0f} pennies')