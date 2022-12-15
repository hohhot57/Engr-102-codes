# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 7.25.1
# Date:         10/10/2022
vowel = ['a','e','i','o','u','A','E','I','O','U','y','Y']
words = str(input(("Enter word(s) to convert to Pig Latin:")))


letter = words.split(" ")
convert = ''

        
for everyword in range(len(letter)):#if the first letter of the user input is a vowel, add yay to the end of "words"
   convert = ''
   if letter[everyword][0] in vowel:
                
      letter[everyword] = letter[everyword] + "yay"
      continue
        
   
   for pig in letter[everyword]:
        if pig not in vowel:
             convert = convert + pig
        else:#if not a vowel, add the first letter of "words" and ay to the end of words
            letter[everyword] = letter[everyword].replace(convert,'',1) + convert + "ay"

            break
        
        
print(f"In Pig Latin,\"{words}\" is: {' '.join(letter)}" )#go through for loop and print out each indi word
        

        