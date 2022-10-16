""" Guess a number Game """

import numpy as np

number = np.random.randint(1,101) # choose a number

# Guessing Process
count = 0

while True: 
    count+=1
    predict_number = int(input("guess a number from 1 to 100: "))
    
    if predict_number > number:
        print("Number should be smaller!")
    
    elif predict_number < number:
        print("Number should be larger!")
        
    else:
        print(f"You guessed it right! The number is = {number} using {count} tries")
        break #end of game
        
        