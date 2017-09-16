### Text Adventure Game

import random as rand

def welcome_message():
    print("~"*65)
    print("Welcome to the 'A Text Adventure Game' game")
    print()
    print("~"*65)
    return

player_HP = 50
player_attk = 10
player_def = 9

###############################################

welcome_message()

print("You are standing in an empty room")
answer1 = input("Will you go left, right, ahead, or behind? ")
if(answer1 == 'right'):
    print("You spot two treasure chests!")
    print()
    print("You opened both chests!")
    rng = rand.randint(0,99)
    if(rng <= 99 and rng >= 90):
        player_attk += 7
    else if (rng <= 89 and rng >= 80):
        player_def += 6
    else if (rng <= 79 and rng >= 70):
        player_HP = 50
    
