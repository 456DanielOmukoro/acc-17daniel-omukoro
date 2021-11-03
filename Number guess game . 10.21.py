'''
Number Guessing Game
'''
import random
import math

# Variables
userNum = 0

# User Input Range
a = int(input('Enter Number: '))
b = int(input('Enter Number: '))

# Upper Lower
if a > b:
    upper = a
    lower = b
else:
    upper = b
    lower = a

# Random Number
randomChoice = random.randint(lower,upper)

# Intro
print(' ')
print('Welcome To The Number Guessing Game')
print('Guess The Random Number')
print(' ')

'''
#Minimum Number of Guesses
minNumberGuesses = round(math.log(upper - lower + 1,2))
print(minNumberGuesses)
'''

# While Loop
while True:
    userNum = int(input('Enter your guess: '))
    if userNum > randomChoice:
        print(' ')
        print('Your Guess Was Too High')
        print('Try Again')
    elif userNum < randomChoice:
        print(' ')
        print('Your Guess Was Too Low')
        print('Try Again')
    else:
        print(' ')
        print('You Win!!!')
        break