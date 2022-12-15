# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jay Ahlschwede
#               Israel Prado
#               Bobby Hao
#               Aidan Murphy
# Section:      525
# Assignment:   3.16 Lab Still More Interpolation
# Date:         9 13 2022



T1= float(input("Enter time 1: \n"))
X1= float(input("Enter the x position of the object at time 1: \n"))
Y1= float(input("Enter the y position of the object at time 1: \n"))
Z1= float(input("Enter the z position of the object at time 1: \n"))
T2= float(input("Enter time 2: \n"))
X2= float(input("Enter the x position of the object at time 2: \n"))
Y2= float(input("Enter the y position of the object at time 2: \n"))
Z2= float(input("Enter the z position of the object at time 2: \n"))

T_Inc= (T2-T1)/4 #The time in between each of five increment

X_Terp1 =X1+(T1-T1)*((X2-X1)/(T2-T1))
X_Terp2 =X1+((T1+T_Inc*1)-T1)*((X2-X1)/(T2-T1))
X_Terp3 =X1+((T1+T_Inc*2)-T1)*((X2-X1)/(T2-T1))
X_Terp4 =X1+((T1+T_Inc*3)-T1)*((X2-X1)/(T2-T1))
X_Terp5 =X1+((T1+T_Inc*4)-T1)*((X2-X1)/(T2-T1))
Y_Terp1 =Y1+(T1-T1)*((Y2-Y1)/(T2-T1))
Y_Terp2 =Y1+((T1+T_Inc*1)-T1)*((Y2-Y1)/(T2-T1))
Y_Terp3 =Y1+((T1+T_Inc*2)-T1)*((Y2-Y1)/(T2-T1))
Y_Terp4 =Y1+((T1+T_Inc*3)-T1)*((Y2-Y1)/(T2-T1))
Y_Terp5 =Y1+((T1+T_Inc*4)-T1)*((Y2-Y1)/(T2-T1))

Z_Terp1 =Z1+((T1+T_Inc*0)-T1)*((Z2-Z1)/(T2-T1))
Z_Terp2 =Z1+((T1+T_Inc*1)-T1)*((Z2-Z1)/(T2-T1))
Z_Terp3 =Z1+((T1+T_Inc*2)-T1)*((Z2-Z1)/(T2-T1))
Z_Terp4 =Z1+((T1+T_Inc*3)-T1)*((Z2-Z1)/(T2-T1))
Z_Terp5 =Z1+((T1+T_Inc*4)-T1)*((Z2-Z1)/(T2-T1))

print(f"At time {T1:.2f} seconds the object is at ({X_Terp1:.3f}, {Y_Terp1:.3f}, {Z_Terp1:.3f})")
print(f"At time {T1+T_Inc*1:.2f} seconds the object is at ({X_Terp2:.3f}, {Y_Terp2:.3f}, {Z_Terp2:.3f})")
print(f"At time {T1+T_Inc*2:.2f} seconds the object is at ({X_Terp3:.3f}, {Y_Terp3:.3f}, {Z_Terp3:.3f})")
print(f"At time {T1+T_Inc*3:.2f} seconds the object is at ({X_Terp4:.3f}, {Y_Terp4:.3f}, {Z_Terp4:.3f})")
print(f"At time {T1+T_Inc*4:.2f} seconds the object is at ({X_Terp5:.3f}, {Y_Terp5:.3f}, {Z_Terp5:.3f})")

