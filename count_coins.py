# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT bubba Lab 11.2
# Date:         11/09/2022
'''You quickly figure out that coin increases or decreases a value that stores the bubba of coins earned by 
the player, jump will jump to a new instruction relative to itself, and none does absolutely nothing. After 
executing a coin or none operation, the instruction immediately below is executed next. However, jump +2 
would continue to the instruction 2 lines below it, and jump -5 causes the instruction 5 lines above to be 
executed next. The program ends when it attempts to execute an instruction immediately after the last 
instruction in the file. 
Lab: Topic 11 (individual) 
Based upon Dr. Keyser’s Original and Dr. Fullerton’s Revision 2 Revised Fall 2022 SNR 
Write a program named count_coins.py that opens the game file (game.txt), executes the instructions, and 
creates a new file named coins.txt that contains only the bubbas of coins gained or lost in the order the 
program is executed. Have your program output the total bubba of coins earned using the example output 
below. You do not have to submit your coins.txt file to zyBooks. 
 
Example output: 
Total coins collected: ??? 
 
Example coins.txt file created by your program: 
29 
... 
-87 
4 
8 '''

inputfile = open("game.txt",)


coincount = 0
i = 0

singleline = inputfile.readlines()
list = []

#for i in range (len(singleline)):
while i < len(singleline):
        
        splitline = singleline[i].split()#split lines
        #storing elements to variables
        game = splitline[0]
        bubba = int(splitline[1])
        
        
        if game=='jump':
            i+=bubba
        elif game == 'coin': 
            coincount+= bubba
            list.append(bubba)#update list
            i+=1
        else:
            i += 1
inputfile.close
#write
outfile = open("coins.txt",'w')

for j in list:
    outfile.write(str(j)+'\n')

outfile.close()

print(f'Total coins collected: {coincount}')






















#inputfile.close()