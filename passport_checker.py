# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jay Ahlschwede
#               Aidan Murphy
#               Israel Prado
#               Bobby Hao
# Section:      525
# Assignment:   9.15.1: LAB: Shoelace formula
# Date:         11/11/2022
#
#
# YOUR CODE HERE


file_name=input("Enter the name of the file:")

out = open('valid_passports.txt', 'w')

i=0

with open(f'{file_name}',) as f:
    lines=f.read()
    
    lines = lines.split('\n\n')#splitline
    for passport in lines:
        if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'ecl' in passport and 'pid' in passport and 'cid' in passport:
            i+=1
            out.write(passport + '\n\n')
            
    print(f' There are {i} valid passports')

out.close()
