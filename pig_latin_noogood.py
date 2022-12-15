# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 7.25.1
# Date:         10/05/2022
#define the list for vowel

vowel = ['a','e','i','o','u','A','E','I','O','U']
#begin the while loop
class piglatin():
    def conversion(engr):
        words = input(("Enter word(s) to convert to Pig Latin:"))
        convert = []
        for everyword in words.split():#if the first letter of the user input is a vowel, add yay to the end of "words"
            if everyword[0] in vowel:
                convert.append(everyword + "yay")
        else:#if not a vowel, add the first letter of "words" and ay to the end of words
            convert.append(everyword[1:] + everyword[0] + "ay")
        
        
        print("In Pig Latin," ,"\"", words,"\"" "is:".join(convert) )
obj1 = piglatin()
obj1.conversion()

#print("In Pig Latin," ,"\"",words,"\"" "is:" , convert)
        
