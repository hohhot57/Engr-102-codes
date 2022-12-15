# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jay Ahlschwede
#               Israel Prado
#               Bobby Hao
# Section:      525
# Assignment:   Lab 3: Unit Conversions
# Date:         9 9 2022
#
#
uservalue=float(input("Please enter the quantity to be converted:"))
lbsC=4.44822
mC=3.28084
atmC=101.325
wattC=3.412142
litsC=15.850323141489
celCm=(9/5)
celCa=32

#x=uservalue*lbsC
#print
x=uservalue*lbsC #for pounds
print(f'{uservalue:.2f} pounds force is equivalent to {x:.2f} Newtons')

x=uservalue*mC #for meters
print(f'{uservalue:.2f} meters is equivalent to {x:.2f} feet')

x=uservalue*atmC
print(f'{uservalue:.2f} atmospheres is equivalent to {x:.2f} kilopascals')

x=uservalue*wattC
print(f'{uservalue:.2f} watts is equivalent to {x:.2f} BTU per hour')

x=uservalue * litsC#for L/s to Galons/h
print(f'{uservalue:.2f} liters per second is equivalent to {x:.2f} US gallons per minute')

x=uservalue * celCm+celCa#for C to F
print(f'{uservalue:.2f} degrees Celsius is equivalent to {x:.2f} degrees Fahrenheit')