### Text Adventure Game
### Room descriptions coming soon

############################ Feedback ############################

import os
import random as r


############################ CLASSES ###############################

### Stats for both player, enemy, and bosses
class stats:

	def __init__(self,HP,MAXHP,MP,MAXMP,atk,intelligence,defense,res,spd,xp,lvl):
		self.HP = HP
		self.MAXHP = MAXHP
		self.MP = MP
		self.MAXMP = MAXMP
		self.atk = atk
		self.intelligence = intelligence
		self.defense = defense
		self.res = res
		self.spd = spd
		self.xp = xp
		self.lvl = lvl

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

	def xp(self):
		return self.xp

	def lvl(self):
		return self.lvl

	def __str__(self):
		return "LVL : % d \nHP/MAXHP: %d/%d MP/MAXMP : %d/%d \nATK : %d \nINT : %d \nDEF : %d \nRES : %d \nSPD : %d \nXP : %d" % (self.lvl,self.HP, self.MAXHP, self.MP,self.MAXMP, self.atk, self.intelligence, self.defense, self.res, self.spd, self.xp)

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
		
###################################################################################################################################################

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
	print("Using your knowledge of the trenches")
	print("You were able to defeat Zheng Yang Pan in a fearsome battle")
	print("Not only that but you were reunited with the love of your life Mercy Kim")
	print("They would leave Zheng Yang Pan's fortress to live happily ever after")
	print("~"*65)
	print("Wow bro. I almost cried from that ending")
	print("Looks like you are such a hardcore gamer")
	print("I wish I had those kinds of moves...")
	print("I hope you had fun playing this basic game :)")
	print("Who knows whats next in store for Quang Le and company...")
	print("~"*65)
	print()
	exit()
	return

def start_game():
	welcome_message()
	player = stats(50,50,30,30,7,6,3,2,5,0,1)
	print()
	print(player)
	player_iven = inventory()
	player_miven = magic_inventory()
	player_miven = rng_magic(player_miven)
	print()
	print(player_miven)
	room_traversal(player,player_miven)


### when you lose possible flag
def game_over():
	print()
	print("You have been defeated...")
	print()
	answer = input("Would you like to try again? ")
	if(answer == "yes"):
		start_game()
	else:
		leaving_message()
		exit()
		return

	
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
		DEF += 15
		RES += 5
		print("You have obtained Zheng Yang's Forbidden Shield!")
		print("You now have " + str(MAXHP) + " HP!")
		print("You now have " + str(ATK) + " ATK!")
		print("You now have " + str(DEF) + " DEF!")
		print("You now have " + str(RES) + " RES!")
	elif (rng < 90 and rng >= 80):  #Ice Knack
		INT += 5
		SPD += 2
		print("You have obtained Ice Knack!")
		print("You now have " + str(INT) + " INT!")
		print("You now have " + str(SPD) + " SPD!")
	elif (rng < 80 and rng >= 60): #worst food
		ATK += 3
		MAXHP += 20
		MAXMP += 20
		print("You have obtained Hugh Brahh's Breastplate!")
		print("You now have " + str(ATK) + " ATK!")
		print("You now have " + str(MAXHP) + " MAX HP!")
		print("You now have " + str(MAXMP) + " MAX MP!")
	elif (rng <= 59 and rng >= 44): #Helm of Pizza Guy
		MAXHP += 5
		ATK += 2
		DEF += 2
		print("You have obtained Helm of Pizza Guy!")
		print("You now have " + str(MAXHP) + " MAX HP!")
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
		print("You now have " + str(MAXHP) + " MAX HP!")
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
		print("You found Mary Jane's Potion of Contentment!")
		print("Your HP has been fully restored!")
	elif(rng < 75 and rng >= 50):
		HP += r.randint(10,15)
		print("You found a counterfeit version of Mary Jane's Potion of Contentment")
		if(HP > MAXHP):
			HP = MAXHP
			print("Your HP has been fully restored")
		else:
			print("Your HP is now " + str(HP))
	elif(rng < 50 and rng >= 25):
		MP = MAXMP
		print("You found The Blue Pill of Dionysus")
		print("Your MP has been fully restored")
	elif(rng < 25 and rng >= 0):
		MP += r.randint(5,10)
		print("You found a counterfeit version of The Blue Pill of Dionysus")
		if(MP > MAXMP):
			MP = MAXMP
			print("Your MP has been fully restored")
		else:
			print("Your MP is now " + str(MP))
	return HP,MAXHP,MP,MAXMP

def enemy_attack(enemy_a,player_a):
	print()
	print("The monster attacks!")
	if(enemy_a.atk - player_a.defense > 0):
		print("You took " + str(enemy_a.atk - player_a.defense) + " damage!")
		player_a.HP -= (enemy_a.atk - player_a.defense)
	else:
		print()
		print("You took no damage!")

############################################### BATTLE SYSTEM redo to include other stats#######################################
def battle_system(playerb,enemyb,playerb_miven):
	print()
	print("A monster approaches!")
	while(playerb.HP > 0 or enemyb.HP > 0):
		print()
		print("Player Stats\n" + str(playerb))
		print()
		print("You can attack, use magic, view the enemy stats, or run")
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
					playerb = enemy_xp(playerb,enemyb)
					#################################################################finishplz##################################################################
					return playerb
				else:
					enemy_attack(enemyb,playerb)
					if(playerb.HP <= 0):
						game_over()
			else:
				enemy_attack(enemyb,playerb)
				if(playerb.HP <= 0):
					game_over()
				if(playerb.atk - enemyb.defense > 0):
					print()
					print("You dealt " + str(playerb.atk - enemyb.defense) + " damage!")
					enemyb.HP -= (playerb.atk - enemyb.defense)
					if(enemyb.HP <= 0):
						print()
						print("You have won the battle!")
						playerb = enemy_xp(playerb,enemyb)
						return playerb
				else:
					print()
					print("You dealt no damage!")
		elif(answer == "view"):
			print()
			print("Enemy Stats\n" + str(enemyb))
			print()
			enemy_attack(enemyb,playerb)
			if(playerb.HP <= 0):
				game_over()

		elif(answer == "magic"):
			if(playerb.MP <= 0):
				print("YOU HAVE NO MANA!!!")
			else:
				print()
				print(playerb_miven)
				answer2 = input("Which spell will you use? ")
				if(playerb.spd > enemyb.spd):
					if(answer2 == "fire blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
						else:
							print("You dealt no damage!\n")

						enemy_attack(enemyb,playerb)
						if(playerb.HP <= 0):
							game_over()
						
					elif(answer2 == "ice blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
						else:
							print("You dealt no damage!\n")

						enemy_attack(enemyb,playerb)
						if(playerb.HP <= 0):
							game_over()
						
					elif(answer2 == "lighting blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
						else:
							print("You dealt no damage!\n")

						enemy_attack(enemyb,playerb)
						if(playerb.HP <= 0):
							game_over()
				
					elif(answer2 == "dunkey blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You used... DUNKEY BLAST!!!")
							print("It should have dealt 100000000000000000 damage but instead it dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
						else:
							print("By some fluke, DUNKEY BLAST!!! did not do anything...")
						enemy_attack(enemyb,playerb)
						if(playerb.HP <= 0):
							game_over()
				else:
					enemy_attack(enemyb,playerb)
					if(playerb.HP <= 0):
						game_over()

					if(answer2 == "fire blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
						else:
							print("You dealt no damage!\n")
					elif(answer2 == "ice blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
						else:
							print("You dealt no damage!\n")
					elif(answer2 == "lighting blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
						else:
							print("You dealt no damage!\n")
					elif(answer2 == "dunkey blast"):
						playerb.MP -= 5
						if(playerb.intelligence > enemyb.res):
							enemyb.HP -= playerb.intelligence - enemyb.res
							print("You used... DUNKEY BLAST!!!")
							print("It should have dealt 100000000000000000 damage but instead it dealt " + str(playerb.intelligence - enemyb.res) + " damage!\n")
							if(enemyb.HP <= 0):
								print()
								print("You have won the battle!")
								playerb = enemy_xp(playerb,enemyb)
								return playerb
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
				enemy_attack(enemyb,playerb)
				if(playerb.HP <= 0):
					game_over()
		else:
			print("That is not a valid option...")
			
def spawn_enemy():
	HP = r.randint(1,25)
	MP = r.randint(5,15)
	enemys = stats(HP,HP,MP,MP,r.randint(5,7),r.randint(3,5),r.randint(2,4),r.randint(2,4),r.randint(5,6),0,1)
	return enemys

def enemy_room(playere,playere_miven):
	E1 = spawn_enemy()
	player_b = battle_system(playere,E1,playere_miven)
	return player_b

def enemy_xp(player_x,enemy_x):
	gain = enemy_x.MAXHP + enemy_x.MAXMP + enemy_x.atk + enemy_x.intelligence + enemy_x.defense + enemy_x.res + enemy_x.spd
	if(gain <= 106 and gain >= 70):
		player_x.xp += 20
	elif(gain < 70 and gain >= 40):
		player_x.xp += 15
	elif(gain < 40):
		player_x.xp += 10
	if(player_x.xp >= 100):
		leftover = 100 - player_x.xp
		player_x.xp = leftover
		player_x.MAXHP += 5 
		player_x.MAXMP += 10
		player_x.atk += 2
		player_x.intelligence += 3
		player_x.defense += 2
		player_x.res += 1
		player_x.lvl += 1
	return player_x

def spawn_final_boss():
	enemys = stats(150,150,50,50,25,15,20,8,15,0,1)
	return enemys

def final_boss(player_fb,player_miven):
	FB = spawn_final_boss()
	player_fb = battle_system(player_fb,FB,player_miven)
	return player_fb

def spawn_first_boss():
	enemy = stats(75,75,20,20,12,2,7,10,9,0,1)
	return enemy

def first_boss(player_fb,player_miven):
	first = spawn_first_boss()
	print()
	print("Chairman Robin Wang blocks your way!")
	playerfb = battle_system(playerfb,first,player_miven)
	return playerfb

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
	
	recov_loot_2 = False
	recov_loot_5 = False
	recov_loot_6 = False
	recov_loot_8 = False
	recov_loot_9 = False
	recov_loot_10 = False
	recov_loot_12 = False

	enemy_r3 = False
	enemy_r4 = False
	enemy_r6 = False
	enemy_r7 = False
	enemy_r8 = False
	enemy_r10 = False

	trap_1L = False
	trap_5R = False
	trap_11L = False

	first_defeat = False
	
	while(room_number < 14):
		print()
		print("You can go left, right, ahead, behind, or view your character")
		answer = input("What will you do? ")
		print()
		
		if(answer == "view"):
			print("~"*65)
			print("Quang Le's Stats")
			print("~"*65)
			print(player_rt)
			print("~"*65)
			print()
			print("Magic Spells")
			print(player_miven)
			print("~"*65)
		############################### ROOM 1 ################################
		elif(answer == "behind" and room_number == 1):
			dead_end()
		elif((answer == "left") and room_number == 1):
			if(trap_1L == False):
				trap_1L = True
				new = trap(player_rt.HP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,new[1],player_rt.intelligence,new[2],player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl) 
			else:
				print("I don't think you want to go back in there...")
		elif(answer == "right" and room_number == 1):
			room_number = 2
			if(get_treasure_2 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
				get_treasure_2 = True
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		elif(answer == "ahead" and room_number == 1):
			room_number = 3
			if(enemy_r3 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r3 = True
				else:
					enemy_r3 = False
			else:
				print("There's nothing here...")


		############################### ROOM 2 ################################
		elif(answer == "right" and room_number == 2):
			dead_end()
		elif(answer == "behind" and room_number == 2):
			if(recov_loot_2 == False):
				recov_loot_2 = True
				new = recovery_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP)
				player_rt = stats(new[0],new[1],new[2],new[3],player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("I don't think an empty chest is useful for adventures")
				print("You already took the treasure")
		elif(answer == "left" and room_number == 2):
			room_number = 1
		elif(answer == "ahead" and room_number == 2):
			room_number = 3
			if(enemy_r3 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r3 = True
				else:
					enemy_r3 = False
			else:
				print("There's nothing here...")
		

		############################### ROOM 3 ################################
		elif(answer == "left" and room_number == 3):
			 dead_end()
		elif(answer == "right" and room_number == 3):
			room_number = 2
			if(get_treasure_2 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
				get_treasure_2 = True
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		elif(answer == "behind" and room_number == 3):
			room_number = 1
		elif(answer == "ahead" and room_number == 3):
			room_number = 4
			if(enemy_r4 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r4 = True
				else:
					enemy_r4 = False
			else:
				print("There's nothing here...")
		

		############################### ROOM 4 ################################
		elif(answer == "left" and room_number == 4):
			dead_end()
		elif(answer == "behind" and room_number == 4):

			room_number = 3
			if(enemy_r3 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r3 = True
				else:
					enemy_r3 = False
			else:
				print("There's nothing here...")

		elif(answer == "ahead" and room_number == 4):
			room_number = 5
			if(get_treasure_5 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
				get_treasure_5 = True
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		elif(answer == "right" and room_number == 4):
			room_number = 7
			if(enemy_r7 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r7 = True
				else:
					enemy_r7 = False
			else:
				print("There's nothing here...")
		

		############################### ROOM 5 ################################
		elif(answer == "left" and room_number == 5):
			dead_end()
		elif(answer == "right" and room_number == 5):
			if(recov_loot_5 == False):
				recov_loot_5 = True
				new = recovery_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP)
				player_rt = stats(new[0],new[1],new[2],new[3],player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("I don't see anything...")
				print("Must mean its empty")
				print("You already took the treasure")

		elif(answer == "ahead" and room_number == 5):
			if(trap_5R == False):
				trap_5R = True
				new = trap(player_rt.HP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,new[1],player_rt.intelligence,new[2],player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("I don't think you want to go back in there...")
		elif(answer == "behind" and room_number == 5):
			room_number = 4
			if(enemy_r4 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r4 = True
				else:
					enemy_r4 = False
			else:
				print("There's nothing here...")
		

		############################### ROOM 6 ################################
		elif(answer == "ahead" and room_number == 6):
			dead_end()
		elif(answer == "left" and room_number == 6):
			if(recov_loot_6 == False):
				recov_loot_6 = True
				new = recovery_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP)
				player_rt = stats(new[0],new[1],new[2],new[3],player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("This chest is looking pretty empty")
				print("You already took the treasure")
		elif(answer == "right" and room_number == 6):
			room_number = 9
			if(get_treasure_9 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
				get_treasure_9 = True
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		elif(answer == "behind" and room_number == 6):
			room_number = 7
			if(enemy_r7 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r7 = True
				else:
					enemy_r7 = False
			else:
				print("There's nothing here...")


		############################### ROOM 7 ################################
		elif(answer == "behind" and room_number == 7):
			dead_end()
		elif(answer == "left" and room_number == 7):
			room_number = 4
			if(enemy_r4 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r4 = True
				else:
					enemy_r4 = False
			else:
				print("There's nothing here...")

		elif(answer == "ahead" and room_number == 7):
			room_number = 6
			if(enemy_r6 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r6 = True
				else:
					enemy_r6 = False
			else:
				print("There's nothing here...")

		elif(answer == "right" and room_number == 7):
			room_number = 8
			if(enemy_r8 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r8 = True
				else:
					enemy_r8 = False
			else:
				print("There's nothing here...")


		############################### ROOM 8 ################################
		elif(answer == "ahead" and room_number == 8):
			dead_end()
		elif(answer == "right" and room_number == 8):
			if(recov_loot_8 == False):
				recov_loot_8 = True
				new = recovery_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP)
				player_rt = stats(new[0],new[1],new[2],new[3],player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("It's time to stop looking because this chest is empty")
				print("You already took the treasure")
		elif(answer == "left" and room_number == 8):
			room_number = 7
			if(enemy_r7 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r7 = True
				else:
					enemy_r7 = False
			else:
				print("There's nothing here...")

		elif(answer == "behind" and room_number == 8):
			room_number = 12
			if(get_treasure_12 == False):
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
				get_treasure_12 = True
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		

		############################### ROOM 9 ################################
		elif(answer == "ahead" and room_number == 9):
			dead_end()
		elif(answer == "behind" and room_number == 9):
			if(recov_loot_9 == False):
				recov_loot_9 = True
				new = recovery_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP)
				player_rt = stats(new[0],new[1],new[2],new[3],player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("Nope, this chest is still empty")
				print("You already took the treasure")
		elif(answer == "left" and room_number == 9):
			room_number = 6
			if(first_defeat == False):
				player_rt = first_boss(player_rt,player_miven)
				first_defeat = True
			else:
				if(enemy_r6 == False):
					temp = player_rt.xp
					player_rt = enemy_room(player_rt,player_miven)
					now = player_rt.xp
					if(temp != now):
						enemy_r6 = True
					else:
						enemy_r6 = False
				else:
					print("There's nothing here...")
		elif(answer == "right" and room_number == 9):
			room_number = 10
			if(enemy_r10 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r10 = True
				else:
					enemy_r10 = False
			else:
				print("There's nothing here...")
		

		############################### ROOM 10 ################################
		elif(answer == "right" and room_number == 10):
			dead_end()
		elif(answer == "ahead" and room_number == 10):
			if(recov_loot_10 == False):
				recov_loot_10 = True
				new = recovery_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP)
				player_rt = stats(new[0],new[1],new[2],new[3],player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("OH LOOK THERE'S SOMETHING IN HERE!")
				print("It's air...")
				print("You already took the treasure")
		elif(answer == "left" and room_number == 10):
			room_number = 9
			if(get_treasure_9 == False):
				get_treasure_9 = True
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		elif(answer == "behind" and room_number == 10):
			room_number = 11
			if(get_treasure_11 == False):
				get_treasure_11 = True
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		

		############################### ROOM 11 ################################
		elif((answer == "behind" or answer == "right") and room_number == 11):
			dead_end()
		elif(answer == "left" and room_number == 11):
			if(trap_11L == False):
				trap_11L = True
				new = trap(player_rt.HP,player_rt.atk,player_rt.defense)
				player_rt = stats(new[0],player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,new[1],player_rt.intelligence,new[2],player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("I don't think you want to go back in there...")
		elif(answer == "ahead" and room_number == 11):
			room_number = 10
			if(get_treasure_10 == False):
				get_treasure_10 = True
				new = rng_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP,player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd)
				player_rt = stats(new[0],new[1],new[2],new[3],new[4],new[5],new[6],new[7],new[8],player_rt.xp,player_rt.lvl)
			else:
				print("Turn around, my african american brother")
				print("There's nothing for you here...")
		

		############################### ROOM 12 ################################
		elif(answer == "left" and room_number == 12):
			dead_end()
		elif(answer == "right" and room_number == 12):
			if(recov_loot_12 == False):
				recov_loot_12 = True
				new = recovery_loot(player_rt.HP,player_rt.MAXHP,player_rt.MP,player_rt.MAXMP)
				player_rt = stats(new[0],new[1],new[2],new[3],player_rt.atk,player_rt.intelligence,player_rt.defense,player_rt.res,player_rt.spd,player_rt.xp,player_rt.lvl)
			else:
				print("Did you expect the treasure to respawn or something?")
				print("You already took the treasure")
		elif(answer == "ahead" and room_number == 12):
			room_number = 8
			if(enemy_r8 == False):
				temp = player_rt.xp
				player_rt = enemy_room(player_rt,player_miven)
				now = player_rt.xp
				if(temp != now):
					enemy_r8 = True
				else:
					enemy_r8 = False
			else:
				print("There's nothing here...")

		elif(answer == "behind" and room_number == 12):
			room_number = 13
			player_rt = enemy_room(player_rt,player_miven)
			print()
			print("ZHENG YANG PAN appears before you!")
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

player = stats(50,50,30,30,7,6,3,2,5,0,1)
print()
print(player)
player_iven = inventory()
player_miven = magic_inventory()
player_miven = rng_magic(player_miven)
print()
print(player_miven)
room_traversal(player,player_miven)