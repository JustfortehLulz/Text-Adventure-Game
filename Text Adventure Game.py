### Text Adventure Game
### Room descriptions coming soon
### make a map

############################ Feedback ##############################
### add xp
### possible items tab
### abilities
### Sunday, September 24th
### finish battle system
### Add Chairman Mao

import random as r

############################ CLASSES ###############################

### Stats for both player, enemy, and bosses
class stats:

	def __init__(self,HP,MAXHP,MP,MAXMP,atk,intelligence,defense,res,spd):
		self.HP = HP
		self.MAXHP = MAXHP
		self.MP = MP
		self.MAXMP = MAXMP
		self.atk = atk
		self.intelligence = intelligence
		self.defense = defense
		self.res = res
		self.spd = spd

	def HP(self):
		return self.HP

	def MAXHP(self):
		return self.MAXHP

	def MP(self):
		return self.MP

	def MAXMP(self):
		return self.MP

	def atk(self):
		return self.atk

	def intelligence(self): return self.intelligence
	
	def defense(self):
		return self.defense

	def res(self):
		return self.res

	def spd(self):
		return self.spd

	def __str__(self):
		return "HP/MAXHP: %d/%d MP/MAXMP : %d/%d \nATK : %d \nINT : %d \nDEF : %d \nRES : %d \nSPD : %d" % (self.HP, self.MAXHP, self.MP,self.MAXMP, self.atk, self.intelligence, self.defense, self.res, self.spd)

##########################LKfjdkljglkfdjkldsjfklsjfksjdkfdjsfklj
class magic:

	def __init__(self,Name,MPCost,DMG):
		self.Name = Name
		self.MPCost = MPCost
		self.DMG = DMG

	def name(self):
		return self.name

	def MPCost(self):
		return self.MPCost

	def DMG(self):
		return self.DMG

	def __str__(self):
		return "Name : %s MPCost : %d DMG : %d" % (self.Name,self.MPCost,self.DMG)

class magic_inventory:

	def __init__(self):
		self.magic = {}

	def add_magic(self,spell):
		self.magic[spell.name] = spell

	def size_m_inven(self):
		return(len(self.magic))

	def __str__(self):
		out = '\t'.join(['Name', 'MPCost', 'DMG'])
		for spell in self.magic.values():
			out += '\n' + '\t'.join([str(x) for x in [spell.Name, spell.MPCost, spell.DMG]])
		return out

class items:

	def __init__(self,name,HP,ATK,DEF):
		self.name = name
		self.HP = HP
		self.ATK = ATK
		self.DEF = DEF

	def name(self):
		return self.name

	def HP(self):
		return self.HP

	def ATK(self):
		return self.ATK

	def DEF(self):
		return self.DEF

	def __str__(self):
		return "Name : %s HP : %d ATK : %d DEF : %d" % (self.name,self.HP,self.ATK,self.DEF)
	
class inventory:

	def __init__(self):
		self.items = {}

	def add_item(self,item):
		self.items[item.name] = item

	def __str__(self):
		out = '\t'.join(['Name', 'HP', 'ATK', 'DEF'])
		for item in self.items.values():
			out += '\n' + '\t'.join([str(x) for x in [item.name, item.HP, item.ATK, item.DEF]])
		return out
		

###### FUNCTIONS ######

### Welcome message
def welcome_message():
	print()
	print("~"*65)
	print("Welcome to the 'A Text Adventure Game' game")
	print("~"*65)
	print()
	print("You are Quang Le.")
	print("The evil lord Zheng Yang Pan has stolen the love of your life, Mercy Kim.")
	print("Using your forbidden knowledge.")
	print("You have inflitrated his fortress.")
	print("You will show him no Mercy and reclaim your love.")
	return

### Leaving message
def leaving_message():
	print()
	print("~"*65)
	print("Hope you had fun! :D")
	print("~"*65)
	print()
	return

### Ending
def fin():
	print()
	print("~"*65)
	print("Wow bruv. You such a hardcore gamer")
	print("I wish I had those kinds of moves...")
	print("I hope you had fun playing this basic game :)")
	print("~"*65)
	print()
	exit()
	return

### when you lose possible flag
def game_over():
	print()
	print("You have been defeated...")
	print()
	answer = input("Would you like to try again? ")
	if(answer == "yes"):
		player_n,room_number = reset()
		welcome_message()
		return player_n,room_number
	else:
		leaving_message()
		exit()
		return

def reset():
	player_reset = stats(50,7,3)
	room_number = 1
	return player_reset,room_number 
	
### rng looting items only
def rng_loot(HP,MAXHP,MP,MAXMP,ATK,INT,DEF,RES,SPD):
	print("You spot a treasure chest!")
	print()
	print("You opened the chest!")
	print()
	rng = r.randint(0,100)
	if(rng <= 100 and rng >= 95): #The Sword of Minh
		ATK += 10
		DEF += 3
		print("You have obtained The Sword of Minh!")
		print("You now have " + str(ATK) + " ATK!")
		print("You now have " + str(DEF) + " DEF!")
	elif (rng < 95 and rng >= 90):  #Zheng Yang's Forbidden Shield
		MAXHP += 15
		ATK += 3
		DEF += 20
		RES += 10
		print("You have obtained Zheng Yang's Forbidden Shield!")
		print("You now have " + str(MAXHP) + " HP!")
		print("You now have " + str(ATK) + " ATK!")
		print("You now have " + str(DEF) + " DEF!")
		print("You now have " + str(RES) + " RES!")
	elif (rng < 90 and rng >= 80):  #best food
		INT += 5
		SPD += 2
		print("You have obtained Ice Knack!")
		print("You now have " + str(INT) + " INT!")
		print("You now have " + str(SPD) + " SPD!")
	elif (rng < 80 and rng >= 60): #worst food
		ATK += 3
		SPD += 1
		MAXMP += 20
		print("You have obtained Gazoolgo!")
		print("You now have " + str(ATK) + " ATK!")
		print("You now have " + str(SPD) + " SPD!")
		print("You now have " + str(MAXMP) + " MAX MP!")
	elif (rng <= 59 and rng >= 44): #Helm of Pizza Guy
		MAXHP += 5
		ATK += 2
		DEF += 2
		print("You have obtained Helm of Pizza Guy!")
		print("You now have " + str(MAXHP) + " HP!")
		print("You now have " + str(ATK) + " attack!")
		print("You now have " + str(DEF) + " defense!")
	elif(rng <= 43 and rng >= 15): #Simon's Pan
		ATK += 1
		print("You have obtained Simon's Pan")
		print("You now have " + str(ATK) + " attack!")
	else:
		MAXHP += 7
		DEF += 5
		RES += 2
		print("You have obtained Hong Chen's Chainmail")
		print("You now have " + str(MAXHP) + " HP!")
		print("You now have " + str(DEF) + " defense!")
	return HP,MAXHP,MP,MAXMP,ATK,INT,DEF,RES,SPD

def recovery_loot(HP,MAXHP,MP,MAXMP):
	print("You spot a treasure chest!")
	print()
	print("You opened the chest!")
	print()
	rng = r.randint(0,100)
	if(rng <= 100 and rng >= 75):
		HP = MAXHP
		print("Your HP has been fully restored")
	elif(rng < 75 and rng >= 50):
		HP += r.randint(10,15)
		if(HP > MAXHP):
			HP = MAXHP
			print("Your HP has been fully restored")
		else:
			print("Your HP is now " + str(HP))
	elif(rng < 50 and rng >= 25):
		MP = MAXMP
		print("Your MP has been fully restored")
	elif(rng < 25 and rng >= 0):
		MP += r.randint(5,10)
		if(MP > MAXMP):
			MP = MAXMP
			print("Your MP has been fully restored")
		else:
			print("Your MP is now " + str(MP))
	return HP,MAXHP,MP,MAXMP


############################################### BATTLE SYSTEM redo to include other stats#######################################
def battle_system(playerb,enemyb,playerb_miven):
	print()
	print("A monster approaches!")
	while(playerb.HP > 0 or enemyb.HP > 0):
		print()
		print("Player Stats\n" + str(playerb))
		print()
		answer = input("What will you do? ")
		if(answer == "attack"):
			if(playerb.spd > enemyb.spd): 
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
					if(enemyb.atk - playerb.defense > 0):
						print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
						playerb.HP -= (enemyb.atk - playerb.defense)
						if(playerb.HP <= 0):
							game_over()
							break
					else:
						print()
						print("You took no damage!")
			else:
				print()
				print("The monster attacks!")
				if(enemyb.atk - playerb.defense > 0):
					print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
					playerb.HP -= (enemyb.atk - playerb.defense)
					if(playerb.HP <= 0):
						game_over()
						break
				else:
					print()
					print("You took no damage!")
				if(playerb.atk - enemyb.defense > 0):
					print()
					print("You dealt " + str(playerb.atk - enemyb.defense) + " damage!")
					enemyb.HP -= (playerb.atk - enemyb.defense)
					if(enemyb.HP <= 0):
						print()
						print("You have won the battle!")
						return playerb
				else:
					print()
					print("You dealt no damage!")
		elif(answer == "view"):
			print()
			print("Enemy Stats\n" + str(enemyb))
			print()
			print("The monster attacks!")
			if(enemyb.atk - playerb.defense > 0):
				print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
				playerb.HP -= (enemyb.atk - playerb.defense)
				if(playerb.HP <= 0):
					game_over()
					break
			else:
				print()
				print("You took no damage!")
		elif(answer == "magic"):
			print()
			print(playerb_miven)
			answer2 = input("Which spell will you use? ")
			if(playerb.spd > enemyb.spd):
				if(answer2 == "fire blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("You dealt no damage!\n")

					print("The monster attacks!")
					if(enemyb.atk - playerb.defense > 0):
						print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
						playerb.HP -= (enemyb.atk - playerb.defense)
						if(playerb.HP <= 0):
							game_over()
							break
					else:
						print()
						print("You took no damage!")
					
				elif(answer2 == "ice blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("You dealt no damage!\n")

					print("The monster attacks!")
					if(enemyb.atk - playerb.defense > 0):
						print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
						playerb.HP -= (enemyb.atk - playerb.defense)
						if(playerb.HP <= 0):
							game_over()
							break
					else:
						print()
						print("You took no damage!")
					
				elif(answer2 == "lighting blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("You dealt no damage!\n")

					print("The monster attacks!")
					if(enemyb.atk - playerb.defense > 0):
						print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
						playerb.HP -= (enemyb.atk - playerb.defense)
						if(playerb.HP <= 0):
							game_over()
							break
					else:
						print()
						print("You took no damage!")
			
				elif(answer2 == "dunkey blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You used... DUNKEY BLAST!!!")
						print("It should have dealt 100000000000000000 damage but instead it dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("By some fluke, DUNKEY BLAST!!! did not do anything...")

					print("The monster attacks!")
					if(enemyb.atk - playerb.defense > 0):
						print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
						playerb.HP -= (enemyb.atk - playerb.defense)
						if(playerb.HP <= 0):
							game_over()
							break
					else:
						print()
						print("You took no damage!")
						
			else:
				print("The monster attacks!")
				if(enemyb.atk - playerb.defense > 0):
					print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
					playerb.HP -= (enemyb.atk - playerb.defense)
					if(playerb.HP <= 0):
						game_over()
						break
				else:
					print()
					print("You took no damage!")

				if(answer2 == "fire blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("You dealt no damage!\n")
				elif(answer2 == "ice blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("You dealt no damage!\n")
				elif(answer2 == "lighting blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("You dealt no damage!\n")
				elif(answer2 == "dunkey blast"):
					playerb.MP -= 5
					if(playerb.intelligence > enemyb.res):
						enemyb.HP -= playerb.intelligence - enemyb.res
						print("You used... DUNKEY BLAST!!!")
						print("It should have dealt 100000000000000000 damage but instead it dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
					else:
						print("By some fluke, DUNKEY BLAST!!! did not do anything...")
						
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
				if(enemyb.atk - playerb.defense > 0):
					print("You took " + str(enemyb.atk - playerb.defense) + " damage!")
					playerb.HP -= (enemyb.atk - playerb.defense)
					if(playerb.HP <= 0):
						game_over()
						break
				else:
					print()
					print("You took no damage!")
		else:
			print("That is not a valid option...")
			
def spawn_enemy():
	HP = r.randint(1,50)
	MP = r.randint(5,15)
	enemys = stats(HP,HP,MP,MP,r.randint(5,10),r.randint(3,10),r.randint(2,6),r.randint(2,5),r.randint(5,10))
	return enemys

def spawn_boss():
	enemys = stats(150,150,50,50,25,15,20,8,15)
	return enemys

def enemy_room(playere,playere_miven):
	E1 = spawn_enemy()
	player_b = battle_system(playere,E1,playere_miven)
	return player_b

def final_boss(player_fb,player_miven):
	FB = spawn_boss()
	player_fb = battle_system(player_fb,FB,player_miven)
	return player_fb

def dead_end():
	print()
	print("There is nothing there...")
	print()
	return

def trap(HP,ATK,DEF):
	print()
	print("You activated a trap!")
	print()
	rng = r.randint(0,100)
	if(rng <= 100 and rng >= 80):
		print("You got scorched by a flamethrower!")
		HP -= 5
	elif(rng <= 79 and rng >= 50):
		print("An arrow from out of nowhere hits your weapon!")
		print("It looks badly damaged...")
		ATK -= 3
	elif(rng <= 49 and rng >= 20):
		print("You were minding your own business when acid fell on your armor!")
		DEF -= 2
	else:
		print("Looks like this trap has already been activated...")
	print("You return to room you were previously in...")
	return HP,ATK,DEF

def rng_magic(player_inven_M):
	print()
	print("You have been bestowed 2 random spells from the Bulalakaw priests!")
	s1 = False
	s2 = False
	s3 = False
	s4 = False
	while(player_inven_M.size_m_inven() < 2):
		rng = r.randint(0,100)
		if(rng <= 100 and rng >= 75 and s1 == False):
			s1 = True
			s1_name = magic("Fire Blast",5,10)
			player_inven_M.add_magic(s1_name)
		elif(rng < 75 and rng >= 50 and s2 == False):
			s2 = True
			s2_name = magic("Ice Blast",5,10)
			player_inven_M.add_magic(s2_name)
		elif(rng < 50 and rng >= 25 and s3 == False):
			s3 = True
			s3_name = magic("Lighting Blast",5,10)
			player_inven_M.add_magic(s3_name)
		elif(rng < 25 and rng >= 0 and s4 == False):
			s4 = True
			s4_name = magic("Dunkey Blast",5,10)
			player_inven_M.add_magic(s4_name)
	return player_inven_M
			

def room_traversal(player_rt,player_miven):
	room_number = 1

	get_treasure_2 = False
	get_treasure_5 = False
	get_treasure_9 = False
	get_treasure_10 = False
	get_treasure_11 = False
	get_treasure_12 = False
	
	trap_1L = False
	trap_5R = False
	trap_11L = False
	
	while(room_number < 14):
		print()
		answer = input("Will you go left, right, ahead, or behind? ")
		print()
		############################### ROOM 1 ################################
		if(answer == "behind" and room_number == 1):
			dead_end()
		elif((answer == "left") and room_number == 1):
			if(trap_1L == False):
				trap_1L = True
				new = trap(player_rt.HP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],MAXHP,MP,MAXMP,new[1],INT,new[2],RES,SPD) #####????????????????????//
			else:
				print("I don't think you want to go back in there...")
		elif(answer == "right" and room_number == 1):
			room_number = 2
			if(get_treasure_2 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
				get_treasure_2 = True
			else:
				print("You the best, my african american brother")
		elif(answer == "ahead" and room_number == 1):
			room_number = 3
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 2 ################################
		elif((answer == "right" or answer == "behind") and room_number == 2):
			dead_end()
		elif(answer == "left" and room_number == 2):
			room_number = 1
		elif(answer == "ahead" and room_number == 2):
			room_number = 3
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 3 ################################
		elif(answer == "left" and room_number == 3):
			 dead_end()
		elif(answer == "right" and room_number == 3):
			room_number = 2
			if(get_treasure_2 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
				get_treasure_2 = True
			else:
				print("You the best, my african american brother")
		elif(answer == "behind" and room_number == 3):
			room_number = 1
		elif(answer == "ahead" and room_number == 3):
			room_number = 4
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 4 ################################
		elif(answer == "left" and room_number == 4):
			dead_end()
		elif(answer == "behind" and room_number == 4):
			room_number = 3
			player_rt = enemy_room(player_rt,player_miven)
		elif(answer == "ahead" and room_number == 4):
			room_number = 5
			if(get_treasure_5 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
				get_treasure_5 = True
			else:
				print("You the best, my african american brother")
		elif(answer == "right" and room_number == 4):
			room_number = 7
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 5 ################################
		elif((answer == "right" or answer == "left") and room_number == 5):
			dead_end()
		elif(answer == "ahead" and room_number == 5):
			if(trap_5R == False):
				trap_5R = True
				new = trap(player_rt.HP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],MAXHP,MP,MAXMP,new[1],INT,new[2],RES,SPD)
			else:
				print("I don't think you want to go back in there...")
		elif(answer == "behind" and room_number == 5):
			room_number = 4
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 6 ################################
		elif((answer == "ahead" or answer == "left") and room_number == 6):
			dead_end()
		elif(answer == "right" and room_number == 6):
			room_number = 9
			if(get_treasure_9 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
				get_treasure_9 = True
			else:
				print("You the best, my african american brother")
		elif(answer == "behind" and room_number == 6):
			room_number = 7
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 7 ################################
		elif(answer == "behind" and room_number == 7):
			dead_end()
		elif(answer == "left" and room_number == 7):
			room_number = 4
			player_rt = enemy_room(player_rt,player_miven)
		elif(answer == "ahead" and room_number == 7):
			room_number = 6
			player_rt = enemy_room(player_rt,player_miven)
		elif(answer == "right" and room_number == 7):
			room_number = 8
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 8 ################################
		elif((answer == "ahead" or answer == "right") and room_number == 8):
			dead_end()
		elif(answer == "left" and room_number == 8):
			room_number = 7
			player_rt = enemy_room(player_rt,player_miven)
		elif(answer == "behind" and room_number == 8):
			room_number = 12
			if(get_treasure_12 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
				get_treasure_12 = True
			else:
				print("You the best, my african american brother")
		############################### ROOM 9 ################################
		elif((answer == "ahead" or answer == "behind") and room_number == 9):
			dead_end()
		elif(answer == "left" and room_number == 9):
			room_number = 6
			player_rt = enemy_room(player_rt)
		elif(answer == "right" and room_number == 9):
			room_number = 10
			player_rt = enemy_room(player_rt,player_miven)
		############################### ROOM 10 ################################
		elif((answer == "ahead" or answer == "right") and room_number == 10):
			dead_end()
		elif(answer == "left" and room_number == 10):
			room_number = 9
			if(get_treasure_9 == False):
				get_treasure_9 = True
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
			else:
				print("You the best, my african american brother")
		elif(answer == "behind" and room_number == 10):
			room_number = 11
			if(get_treasure_11 == False):
				get_treasure_11 = True
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
			else:
				print("You the best, my african american brother")
		############################### ROOM 11 ################################
		elif((answer == "behind" or answer == "right") and room_number == 11):
			dead_end()
		elif(answer == "left" and room_number == 11):
			if(trap_11L == False):
				trap_11L = True
				new = trap(player_rt.HP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],MAXHP,MP,MAXMP,new[1],INT,new[2],RES,SPD)
			else:
				print("I don't think you want to go back in there...")
		elif(answer == "ahead" and room_number == 11):
			room_number = 10
			if(get_treasure_10 == False):
				get_treasure_10 = True
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],new[1],new[2],new[3])
			else:
				print("You the best, my african american brother")
		############################### ROOM 12 ################################
		elif((answer == "left" or answer == "right") and room_number == 12):
			dead_end()
		elif(answer == "ahead" and room_number == 12):
			room_number = 8
			player_rt = enemy_room(player_rt,player_miven)
		elif(answer == "behind" and room_number == 12):
			room_number = 13
			player_rt = enemy_room(player_rt,player_miven)
			player_rt = final_boss(player_rt,player_miven)
			fin()
		############################### ERROR ################################
		else:
			print("That is not a valid option...")
		print()
		print("You are currently in room # " + str(room_number))
	return

			
###############################################################################################################################

welcome_message()

player = stats(50,50,30,30,7,6,3,2,5)
print()
print(player)
player_iven = inventory()
player_miven = magic_inventory()
player_miven = rng_magic(player_miven)
print()
print(player_miven)
room_traversal(player,player_miven)
