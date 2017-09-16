### Text Adventure Game
### Room descriptions coming soon

import random as rand

def welcome_message():
    print("~"*65)
    print("Welcome to the 'A Text Adventure Game' game")
    print()
    print("~"*65)
    return

def spawn_enemy():
    print("A monster approaches!")
    enemy_HP = rand.randint(1,20)
    enemy_attk = rand.randint(1,7)
    enemy_def = rand.randint(1,5)
    return enemy_HP,enemy_attk,enemy_def

def battle_system(enemy_HP,enemy_attk,enemy_def,player_HP,player_attk,player_def):
    while(enemy_HP > 0):
        print("Player Stats:")
        print(str(player_HP) + " HP " + str(player_attk) + " Attack " + str(player_def) + " Defense")
        print()
        answer = input("What will you do? ")
        if(answer == "attack"):
            if(player_attk - enemy_def > 0):
                print()
                print("You dealt " + str(player_attk - enemy_def) + " damage!")
                enemy_HP = enemy_HP - (player_attk - enemy_def)
            else:
                print()
                print("You dealt no damage!")
            if(enemy_HP <= 0):
                print()
                print("You have won the battle!")
                print(str(player_HP) + " HP")
                return player_HP
            else:
                print()
                print("The monster attacks!")
                if(enemy_attk - player_def > 0):
                    print("You took " + str(enemy_attk - player_def) + " damage!")
                    player_HP = player_HP - (enemy_attk - player_def)
                else:
                    print()
                    print("You took no damage!")
        elif(answer == "view"):
            print()
            print("Enemy Stats")
            print(str(enemy_HP) + " HP")
            print(str(enemy_attk) + " Attack")
            print(str(enemy_def) + " Defense")
        elif(answer == "run"):
            flee = rand.randint(0,50)
            if(flee > enemy_HP + enemy_attk + enemy_def):
                print()
                print("You have fled from battle!")
                return player_HP
            else:
                print()
                print("The monster blocks your path!")
                print("The monster attacks!")
                if(enemy_attk - player_def > 0):
                    print("You took " + str(enemy_attk - player_def) + " damage!")
                    player_HP = player_HP - (enemy_attk - player_def)
                else:
                    print()
                    print("You took no damage!")
                
            

def rng_loot(player_HP,player_attk,player_def):
    print("You spot a treasure chest!")
    print("You opened the chest!")
    rng = rand.randint(0,99)
    if(rng <= 99 and rng >= 90): #best sword
        player_attk += 7
        print("You have obtained the best sword")
        print("You now have " + str(player_attk) + " attack!")
    elif (rng <= 89 and rng >= 80):  #best shield
        player_def += 6
        print("You have obtained the best shield")
        print("You now have " + str(player_def) + " defense!")
    elif (rng <= 79 and rng >= 70):  #best food
        player_HP = 50
        print("Your health has been fully restored")
    elif (rng <= 69 and rng >= 50): #worst food
        player_HP += rand.randint(10,15)
        if(player_HP > 50):
            player_HP = 50
        print("Your health is now " + str(player_HP))
    elif (rng <= 49 and rng >= 24): #worst sword
        player_attk += 3
        print("You have obtained the worst sword")
        print("You now have " + str(player_attk) + " attack!")
    else: #worst shield
        player_def += 3
        print("You have obtained the worst shield")
        print("You now have " + str(player_def) + " defense!")
    return player_HP,player_attk,player_def

def room_traversal(room_number):
    print("You are in room # " + str(room_number))
    answer = input("Will you go left, right, ahead, or behind? ")
    if(answer == 'right' and room_number == 1):
        room_number = 2
        print(room_number)
        print("after change")
        rng_loot(player_HP,player_attk,player_def)
    elif((answer == 'left' or answer == 'behind') and room_number == 1):
        if (answer == 'left'):
            print("There is nothing to the left of you")
        else:
            print("There is nothing behind you")
    elif((answer == 'ahead') and room_number == 1):
        enemy_HP,enemy_attk,enemy_def = spawn_enemy()
        battle_system(enemy_HP,enemy_attk,enemy_def,player_HP,player_attk,player_def)
        room_number = 3
    elif((answer == 'left') and room_number == 2):
         enemy_HP,enemy_attk,enemy_def = spawn_enemy()
         battle_system(enemy_HP,enemy_attk,enemy_def,player_HP,player_attk,player_def)
         room_number = 1
    elif((answer == 'ahead') and room_number == 2):
         enemy_HP,enemy_attk,enemy_def = spawn_enemy()
         battle_system(enemy_HP,enemy_attk,enemy_def,player_HP,player_attk,player_def)
         room_number = 3
    
    print("You are in room # " + str(room_number))     
    return room_number

#####################################################################################################

welcome_message()

global enemy_HP
global enemy_attk
global enemy_def
player_HP = 50
player_attk = 10
player_def = 9
room_number = 1

print("You are standing in an empty room")
room_number = room_traversal(room_number)

