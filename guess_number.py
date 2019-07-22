import random

hidden_number = random.randint(1, 100)
print("\nLets play ! Try to find a number !")
guess = input('Guess a number: ')
guess = int(guess)

def find(hidden_number, guess):
    while guess != 'quit':
        guess = int(guess)
        if guess < hidden_number:
            guess = input('Try higher or type < quit > : ')
        elif guess > hidden_number:
            guess = input('Try lower or type < quit >: ')
        elif guess == hidden_number:
            print('Congarulations, You found it!')
            return hidden_number
    print('You lost the game ...')
    
find(hidden_number, guess)