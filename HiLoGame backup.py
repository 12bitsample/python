# Michael McAdow
# 7/11/20
# HiLoGame.py
# Program to generate random number within guessing game and ask user if they would like to play game again.

play_game = 'y'
import random

while play_game == 'y':

    number = int(input('\nWhat should the maximum number for this game be? '))
    random_num = random.randint(1,number)
    print(random_num)
    guess_num = int(input('\nGuess my number: '))
    
    
    while guess_num != random_num:
          
        if guess_num > random_num:
            print('Your guess is too high!')
            guess_num = int(input('\nGuess my number: '))
        elif guess_num < random_num:
            print('Your guess is too low!')
            guess_num = int(input('\nGuess my number: '))
        elif guess_num == random_num:
            break

    if guess_num == random_num:
        print('You guessed my number!')       
        
    play_game = str.lower(input('\nDo you wish to play again? (Y/N): '))   
        
if play_game == 'n':
    print('Thanks for playing, goodbye!')
    
