# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Bobby Hao
# Section:      525
# Assignment:   THE ASSIGNMENT NUMBER Lab 10
# Date:         11/04/2022
'''Write a python program named guessing_game.py to play a number guessing game. Have your program 
display a short message with instructions, then continually prompt the user to guess a number. With 
each wrong guess, let the user know if their guess is too high or too low. When the user correctly 
guesses the number, output the total number of guesses made. Write your program using at least two 
(2) functions and a try-except statement. For the purposes of autograding, make your secret number 
26, and use the example output below for the text. 
 
Example output: 
Guess the secret number! Hint: it's an integer between 1 and 100... 
What is your guess? 50 
Too high! 
What is your guess? 12 
Too low! 
What is your guess? 0.5 
Bad input! Try again: 26 
You guessed it! It took you 3 guesses. '''

def func():
    x = 26
    guess = 1
    
    #z = (input("What is your guess?\n"))
    #y = int(input("What is your guess?\n")
    #y = int(input("What is your guess?\n"))
    while guess<6:#found a way to start the while loop
        try:
            y = int(input("What is your guess?\n"))#test if the input is an intger or not
            #while y != x:
            #while p<6:    
            if y > x:
                print("Too high!")
                #y = int(input("What is your guess?\n"))
                guess +=1
                y = int(input("What is your guess?\n"))
                #continue
            if y < x:
                print("Too low!")
                #y = int(input("What is your guess?\n"))
                guess+=1
                y = int(input("What is your guess?\n"))
            #a
            # a
                #continue
            if y==x:
                guess += 1
            # y = tryfunc()
            # p += 1
            # print(f'You guessed it! It took you {p} guesses.')
            #tryfunc()
            #p+=1   
                break
        except ValueError:#if not intger return error but i don't how to make it return back to the loop w/o printing none
        
            y=input(print("Bad input! Try again: "))
            if y ==x:
                print(f'You guessed it! It took you {guess} guesses.')
        # Take input again
                       
    if y==x:
        print(f'You guessed it! It took you {guess} guesses.')
        
                    
                
                
        
            # tryfunc()
            # p+=1
            #print(f'You guessed it! It took you {p} guesses.')
def question():
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
question()
func()




  
    

