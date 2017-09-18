### Work in progress
### Text Adventure Game
### Room descriptions coming soon

### Find a better way to check current state

import random as r

###### CLASSES ######

### Stats for both player, enemy, and bosses
class stats:

    def __init__(self,HP,atk,defense):
        self.HP = HP
        self.atk = atk
        self.defense = defense

    def HP(self):
        return self.HP

    def atk(self):
        return self.atk

    def defense(self):
        return self.defense

    def __str__(self):
        return "HP : %d ATK : %d DEF : %d" % (self.HP, self.atk, self.defense)

###### FUNCTIONS ######

### Welcome message
def welcome_message():
    print()
    print("~"*65)
    print("Welcome to the 'A Text Adventure Game' game")
    print("~"*65)
    print()
    return

### Leaving message
def leaving_message():
    print()
    print("~"*65)
    print("Hope you had fun! :D")
    print("~"*65)
    print()
    return

def fin():
    print()
    print("~"*65)
    print("Wow bruv. You such a hardcore gamer")
    print("I wish I had those kinds of moves...")
    print("I hope you had fun playing this basic game :)")
    print("~"*65)
    print()
    return

### when you lose possible flag
def game_over():
    print()
    print("You have been defeated...")
    print()
    answer = input("Would you like to try again? ")
    if(answer == "yes"):
        welcome_message()
        return
    else:
        leaving_message()
        return

### rng looting
def rng_loot(HP,ATK,DEF):
    print("You spot a treasure chest!")
    print()
    print("You opened the chest!")
    print()
    rng = r.randint(0,99)
    if(rng <= 99 and rng >= 90): #best sword
        ATK += 7
        print("You have obtained the best sword!")
        print("You now have " + str(ATK) + " attack!")
    elif (rng <= 89 and rng >= 80):  #best shield
        DEF += 6
        print("You have obtained the best shield!")
        print("You now have " + str(DEF) + " defense!")
    elif (rng <= 79 and rng >= 70):  #best food
        HP = 50
        print("Your health has been fully restored!")
    elif (rng <= 69 and rng >= 50): #worst food
        HP += r.randint(10,15)
        if(HP > 50):
            HP = 50
        print("Your health is now " + str(HP))
    elif (rng <= 49 and rng >= 24): #worst sword
        ATK += 3
        print("You have obtained the worst sword...")
        print("You now have " + str(ATK) + " attack!")
    else: #worst shield
        DEF += 3
        print("You have obtained the worst shield...")
        print("You now have " + str(DEF) + " defense!")
    return HP,ATK,DEF

### battle system
def battle_system(playerb,enemyb):
    print()
    print("A monster approaches!")
    while(playerb.HP > 0 or enemyb.HP > 0):
        print()
        print("Player Stats\n" + str(playerb))
        print()
        answer = input("What will you do? ")
        if(answer == "attack"):
            if(playerb.atk - enemyb.defense > 0):
                print()
                print("You dealt " + str(playerb.atk - enemyb.defense) + " damage!")
                enemyb.HP -= (playerb.atk - enemyb.defense)
            else:
                print()
                print("You dealt no damage!")
            if(enemyb.HP <= 0):
                print()
                print("You have won the battle!")
                return playerb
            else:
                print()
                print("The monster attacks!")
                if(int(enemyb.atk - playerb.defense) > 0):
                    print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
                    playerb.HP -= (enemyb.atk - playerb.defense)
                    if(playerb.HP <= 0):
                        game_over()
                        break
                else:
                    print()
                    print("You took no damage!")
        elif(answer == "view"):
            print()
            print("Enemy Stats\n" + str(enemyb))
            print()
            print("The monster attacks!")
            if(int(enemyb.atk - playerb.defense) > 0):
                print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
                playerb.HP -= (enemyb.atk - playerb.defense)
                if(playerb.HP <= 0):
                    game_over()
                    break
            else:
                print()
                print("You took no damage!")
        elif(answer == "run"):
            flee = r.randint(0,75)
            if(flee > (enemyb.HP + enemyb.atk + enemyb.defense)):
                print()
                print("You have fled from battle!")
                return playerb
            else:
                print()
                print("The monster blocks your path!")
                print("The monster attacks!")
                if(int(enemyb.atk - playerb.defense) > 0):
                    print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
                    playerb.HP -= (enemyb.atk - playerb.defense)
                    if(playerb.HP <= 0):
                        game_over()
                        break
                else:
                    print()
                    print("You took no damage!")
                
def spawn_enemy():
    enemys = stats(r.randint(1,50),r.randint(1,10),r.randint(1,4))
    return enemys

def spawn_boss():
    enemys = stats(70,25,10)
    return enemys

def enemy_room(playere):
    E1 = spawn_enemy()
    player_b = battle_system(playere,E1)
    return player_b

def final_boss(player_fb):
    FB = spawn_boss()
    player_fb = battle_system(player_fb,FB)
    return player_fb

def dead_end():
    print()
    print("There is nothing there...")
    print()
    return

def room_traversal(player_rt):
    room_number = 1
    while(room_number < 14):
        print()
        answer = input("Will you go left, right, ahead, or behind? ")
        print()
        ############################### ROOM 1 ################################
        if((answer == "left" or answer == "behind") and room_number == 1):
            dead_end()
        elif(answer == "right" and room_number == 1):
            room_number = 2
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        elif(answer == "ahead" and room_number == 1):
            room_number = 3
            player_rt = enemy_room(player_rt)
        ############################### ROOM 2 ################################
        elif((answer == "right" or answer == "behind") and room_number == 2):
            dead_end()
        elif(answer == "left" and room_number == 2):
            room_number = 1
        elif(answer == "ahead" and room_number == 2):
            room_number = 3
            player_rt = enemy_room(player_rt)
        ############################### ROOM 3 ################################
        elif(answer == "left" and room_number == 3):
             dead_end()
        elif(answer == "right" and room_number == 3):
            room_number = 2
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        elif(answer == "behind" and room_number == 3):
            room_number = 1
        elif(answer == "ahead" and room_number == 3):
            room_number = 4
            player_rt = enemy_room(player_rt)
        ############################### ROOM 4 ################################
        elif(answer == "left" and room_number == 4):
            dead_end()
        elif(answer == "behind" and room_number == 4):
            room_number = 3
            player_rt = enemy_room(player_rt)
        elif(answer == "ahead" and room_number == 4):
            room_number = 5
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        elif(answer == "right" and room_number == 4):
            room_number = 7
            player_rt = enemy_room(player_rt)
        ############################### ROOM 5 ################################
        elif((answer == "right" or answer == "ahead" or answer == "left") and room_number == 5):
            dead_end()
        elif(answer == "behind" and room_number == 5):
            room_number = 4
            player_rt = enemy_room(player_rt)
        ############################### ROOM 6 ################################
        elif((answer == "ahead" or answer == "left") and room_number == 6):
            dead_end()
        elif(answer == "right" and room_number == 6):
            room_number = 9
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        elif(answer == "behind" and room_number == 7):
            room_number = 6
            player_rt = enemy_room(player_rt)
        ############################### ROOM 7 ################################
        elif(answer == "behind" and room_number == 7):
            dead_end()
        elif(answer == "left" and room_number == 7):
            room_number = 4
            player_rt = enemy_room(player_rt)
        elif(answer == "ahead" and room_number == 7):
            room_number = 6
            player_rt = enemy_room(player_rt)
        elif(answer == "right" and room_number == 7):
            room_number = 8
            player_rt = enemy_room(player_rt)
        ############################### ROOM 8 ################################
        elif((answer == "ahead" or answer == "right") and room_number == 8):
            dead_end()
        elif(answer == "left" and room_number == 8):
            room_number = 7
            player_rt = enemy_room(player_rt)
        elif(answer == "behind" and room_number == 8):
            room_number = 12
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        ############################### ROOM 9 ################################
        elif((answer == "ahead" or answer == "behind") and room_number == 9):
            dead_end()
        elif(answer == "left" and room_number == 9):
            room_number = 6
            player_rt = enemy_room(player_rt)
        elif(answer == "right" and room_number == 9):
            room_number = 10
            player_rt = enemy_room(player_rt)
        ############################### ROOM 10 ################################
        elif((answer == "ahead" or answer == "right") and room_number == 10):
            dead_end()
        elif(answer == "left" and room_number == 10):
            room_number = 9
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        elif(answer == "behind" and room_number == 10):
            room_number == 11
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        ############################### ROOM 11 ################################
        elif((answer == "ahead" or answer == "left" or answer == "right") and room_number == 11):
            dead_end()
        elif(answer == "behind" and room_number == 11):
            new = rng_loot(player_rt.HP,player_rt.atk,player_rt.defense)
            player_rt = stats(new[0],new[1],new[2])
        ############################### ROOM 12 ################################
        elif((answer == "left" or answer == "right") and room_number == 12):
            dead_end()
        elif(answer == "behind" and room_number == 12):
            room_number = 8
            player_rt = enemy_room(player_rt)
        elif(answer == "ahead" and room_number == 12):
            room_number = 13
            player_rt = enemy_room(player_rt)
            player_rt = final_boss(player_rt)
            fin()
        print()
        print("You are currently in room # " + str(room_number))
    return    

            
###############################################################################################################################

welcome_message()

player = stats(50,7,3)
room_traversal(player)

