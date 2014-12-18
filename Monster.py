import pygame
import random

HalfEffect = ["electricgrass", "firewater", "watergrass", "groundgrass", "grassgrass", "waterwater", "firefire", "electricelectric"]
DoubleEffect = ["electricwater", "waterfire", "waterground", "grasswater", "grassground", "groundfire", "groundelectric"]
NoEffect = ["electricground"]

class Move():
	def __init__(self, name = "", damage = 0, element = "normal"):
		self.name = name
		self.damage = damage
		self.element = element

class Monster():
	def __init__(self, number=1, name = "Missingno", lvl = 1, moves = [Move(),Move(),Move(),Move()], element = "normal", hp = "", exp = 0):
		self.name = name
		self.lvl = lvl
		if hp == "":
			self.hp = 20 + 3 * lvl
		else: 
			self.hp = hp
		self.moves = moves
		self.number = number
		self.element = element
		self.exp = exp
		self.setstats()
		
		
	def setstats(self):
		self.maxhp = 20 + 3 * self.lvl
		self.atk = 2 * self.lvl
		self.defence = self.lvl
        

	def attack(self, other, move):
		Multiplier = 1.
		AM = move.element + other.element

		if AM in HalfEffect: Multiplier = .5
		elif AM in DoubleEffect: Multiplier = 2.
		elif AM in NoEffect: Multiplier = 0.
            
		other.hp -= int(self.atk * move.damage / 10. / (10. + other.defence) * Multiplier) + 1
		if other.hp <0: other.hp = 0
		print "other.hp", other.hp
		print "self.atk", self.atk
		print "move.damage", move.damage
		print "other.defence", other.defence

	def addexp(self, amount, lp):
		self.exp += amount
		if self.exp >= self.lvl ** 2:
			self.exp -= self.lvl ** 2
			self.lvl += 1
			self.setstats()
			print "Your %s has leveled up to %s!" % (self.name, str(self.lvl))
			lp.addtochat("Your %s has leveled up to %s!" % (self.name, str(self.lvl)))
			self.hp += 3

def getWildMonster():
    return random.choice(["Broseidon","Brometer","Brollo","Brophaestus","Brous","Brothena"])
    
def getMove(name):
	if name=="Tackle":
		return Move("Tackle", 50, "normal")
	if name=="Splash":
		return Move("Splash", randint(0,100), "normal")
	if name=="Bitch Slap":
		return Move("Bitch Slap", 30*randint(2,3), "normal")
	if name=="Trifecta":
		return Move("Trifecta", 50*randint(1,2), "normal")
	if name=="Double Edge":
		return Move("Double Edge", 80, "normal")
	elif name=="Surf":
		return Move("Surf", 80, "water")
	elif name=="Rain":
		return Move("Rain", 20*randint(2,6), "water")
	elif name=="Flamethrower":
		return Move("Flamethrower", 80, "fire")
	elif name=="Fire Pellet":
		return Move("Fire Pellet", 20*randint(2,6), "fire")
	elif name=="Razor Leaf":
		return Move("Razor Leaf", 80, "grass")
	elif name=="Bullet Seed":
		return Move("Bullet Seed", 20*randint(2,6), "grass")
	elif name=="Thunderbolt":
		return Move("Thunderbolt", 80, "electric")
	elif name=="Multispark":
		return Move("Multispark", 20*randint(2,6), "electric")
	elif name=="Earthquake":
		return Move("Earthquake", 80, "earth")
	elif name=="Aftershocks":
		return Move("Aftershocks", 20*randint(2,6), "ground")
	elif name=="Part the Red Sea":
		return Move("Part the Red Sea", 2000, "water")
	elif name=="Go Super Saiyan":
		return Monve("Go Super Saiyan", 1, "electric")
	elif name=="Trolololol":
		return Monve("Trolololol", 0, "normal")
	
		
def getMonster(name, lvl = 1, hp = "", exp = 0):
	if name=="Broseidon":
		return Monster(1, "Broseidon",lvl,[getMove("Surf"),getMove("Rain"),getMove("Tackle"),getMove("Splash")],"water", hp, exp)
	if name=="Brometer":
		return Monster(2, "Brometer",lvl,[getMove("Razor Leaf"),getMove("Bullet Seed"),getMove("Tackle"),getMove("Splash")],"grass", hp, exp)
	if name=="Brollo":
		return Monster(3, "Brollo",lvl,[getMove("Flamethrower"),getMove("Fire Pellet"),getMove("Tackle"),getMove("Splash")],"fire", hp, exp)
	if name=="Brophaestus":
		return Monster(4, "Brophaestus",lvl,[getMove("Earthquake"),getMove("Aftershocks"),getMove("Tackle"),getMove("Splash")],"ground", hp, exp)
	if name=="Broos":
		return Monster(5, "Brous",lvl,[getMove("Thunderbolt"),getMove("Multispark"),getMove("Tackle"),getMove("Splash")],"electric", hp, exp)
	if name=="Brothena":
		return Monster(6, "Brothena",lvl,[getMove("Double Edge"),getMove("Bitch Slap"),getMove("Trifecta"),getMove("Splash")],"normal", hp, exp)
	if name=="Broses":
		return Monster(99, "Broses",lvl,[getMove("Part the Red Sea"),getMove("Trolololol"),getMove("Tackle"),getMove("Splash")],"water", hp, exp)
	if name=="Broku":
		return Monster(99, "Broku",lvl,[getMove("Go Super Saiyan"),getMove("Trolololol"),getMove("Tackle"),getMove("Splash")],"electric", hp, exp=0)
	
