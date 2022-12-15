# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
#  Groups Names:
#               Israel Prado
#               Jay Ahlschwede
#               Bobby Hao
#               Aidan Murphy
# Section:      525
# Assignment:   Lab11 Part B
# Date:         11 11 2022
#



#NOTE THIS CODE IS NOT FUNCTIONAL
file_name=input("Enter the name of the file: ")

out = open('valid_passports.txt', 'w')

i=0

with open(f'{file_name}','r') as f:
    lines=f.read()
    
    lines = lines.split('\n\n')
    for passport in lines:
        if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'ecl' in passport and 'pid' in passport and 'cid' in passport:
            out.write(passport + '\n\n')
            
out.close()
i=0
vaild_pass=0
portlist=[]

with open('valid_passports.txt','r') as file:
    lines=file.read()
    lines_list = lines.split('\n\n')
    while i < len(lines_list):#runs through entire list
        portlist += [lines_list[i].replace('\n',' ')]
        i+=1
d=0 
valpass=0
k=0      
while k <len(portlist):
    cons=portlist[k]
    clist=cons.split()
    vc=0
    for char in clist:
        ctype=char[:3]
        if ctype=='byr':
            v=int(char[4:])
            if (v>=1920) and (v<=2005):
                vc+=1
        if ctype=='iyr':
            v=int(char[4:])
            if (v>=2012) and (v<=2022):
                vc+=1
        if ctype=='eyr':
            v=int(char[4:])
            if (v>=2022) and (v<=2032):
                vc+=1
        if ctype=='hgt':
            try:
                t=char[-2]
                v=int(char[4:-2])
                if (t=='c') and (v>=150) and (v<=193):
                    vc+=1
                if (t=='i') and (v>=59) and (v<=76):
                    vc+=1
            except:
                b=4
        if ctype=='ecl':
            v=char[4:]
            if v == 'amb' or 'blu' or 'brn' or 'gry' or 'grn' or 'hzl' or 'oth':
                vc+=1
        if ctype=='pid':
            v=char[4:]
            if len(v)==9:
                vc+=1 
        if ctype=='cid':
            vipe=str(char[4:])
            v=vipe.lstrip('0')
            if len(v)==3:
                vc+=1
        if vc==7:
            valpass+=1
    k+=1


print(f'There are {valpass} valid passports')

