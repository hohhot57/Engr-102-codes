vowel = ['a','e','i','o','u','A','E','I','O','U']
#begin the while loop
def main():
    while True:
        words = input(("Enter word(s) to convert to Pig Latin:"))
        convert = []

        for everyword in words.split():#if the first letter of the user input is a vowel, add yay to the end of "words"
            if everyword[0] in vowel:
                convert.append(everyword + "yay")
            else:#if not a vowel, add the first letter of "words" and ay to the end of words
                  convert.append(everyword[1:] + everyword[0] + "ay")
        
        
        print("In Pig Latin," ,"\"", everyword ,"\"" "is:", convert )

main()


#print("In Pig Latin," ,"\"",words,"\"" "is:" , convert)
        