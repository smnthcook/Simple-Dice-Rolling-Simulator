'''
Simple Dice Rolling Simulator
Samantha Cook
4/25/2023
'''

import random, time # - import modules "random" and "time"

def load(seconds):
    '''
    Prints a line every half-second.
    '''
    loading = ['-', '/', '|', '\\', '-',  ]
    for i in range(len(loading)):
        print(loading[i])
        time.sleep(seconds)

def rolling_dice():
    '''
    Gets a random number 1-6; "rolling" the di.
    '''
    dice = 0
    dice = random.randint(1, 6)
    print('You rolled a', dice, '!')
    


#main
repeat = 'y'
while repeat == 'y': #sets up the while loop; loops when "y" is entered in terminal. 
    print('Release!')
    load(.5)
    rolling_dice()
    repeat = input('Would you like to roll again? (y/n) >> ').lower()


