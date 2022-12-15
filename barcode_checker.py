# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 11.1
# Date:         11/09/2022

'''A barcode is valid if the digits satisfy a certain constraint. For example, take the 13-digit barcode 
1877455846014 and split the first 12 digits into two groups: (1,7,4,5,4,0) and (8,7,5,8,6,1). 
The first group contains every other digit starting with the first, and the second group contains every other 
digit starting with the second. Take the sum of the digits in the second group, and multiply it by 3. Add to that 
the sum of the digits in the first group. Subtract the last digit of that number from 10, and it should match the 
last digit of the barcode. 
 
Example math using barcode 1877455846014: 
Sum of first group = 1 + 7 + 4 + 5 + 4 + 0 = 21 
Sum of second group = 8 + 7 + 5 + 8 + 6 + 1 = 35 
Multiply second group by 3 = 35 x 3 = 105 
Add first group = 105 + 21 = 126 
Use the last digit and subtract from ten = 10 - 6 = 4 
4 is the last digit in the barcode, so it is valid '''


def goodbar(givencode):
    
    first_group = [int(givencode[i]) for i in range(0, 12, 2)]
    second_group = [int(givencode[i]) for i in range(1, 12, 2)]
    #first_group = int(barcode[i])
    

 #   print(f'Sum of first group: {sum(first_group)}')
  ##  print(f'Sum of second group: {sum(second_group)}')
  #  print(f'Multiply second group by 3 = {sum(second_group)} x 3 ={sum(second_group) * 3}' )
  #  print(f'Add first group = {sum(second_group) * 3} + {sum(first_group)}')
   
    
    notall = (sum(second_group) * 3 + sum(first_group)) % 10
    #notall2 = int(barcode[-1]) 
#subtract= notall - notall2
    #everything = notall == 10 - notall2
   # print(f'Use the last digit and subtract from ten = {10} - {notall} = {10-notall}\n')
    everything = (sum(second_group) * 3 + sum(first_group)) % 10 == 10 - int(givencode[-1])
    return everything

def goodfunc():
    inputfile = (input("Enter the name of the file: "))

    readfile = open(inputfile,)
    writefile = open('valid_barcodes.txt','w')
    goodcodes = 0
    for i in readfile:
        if goodbar(i.strip()):
            goodcodes += 1
            writefile.write(i)      
    print(f"There are {goodcodes} valid barcodes",)

    readfile.close()
    writefile.close()
goodfunc()