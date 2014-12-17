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
    return random.choice(["","","",""])
def getMove(name):
	if name=="Tackle":
		return Monstermove("Tackle", 60, "normal")
	elif name=="Surf":
		return Monstermove("Surf", 90, "water")
	elif name=="Flamethrower":
		return Pokemove("Flamethrower", 90, "fire")
	elif name=="Razor Leaf":
		return Monstermove("Razor Leaf", 90, "grass")
	elif name=="Thunderbolt":
		return Monstermove("Thunderbolt", 90, "electric")
	elif name=="Earthquake":
		return Monstermove("Earthquake", 90, "earth")
		
def getMonster(name, lvl = 1, hp = "", exp = 0):
    if name=="":
        return Pokemon(1, "",lvl,[getMove(""),getMove(""),getMove(""),getMove("")],"", hp, exp)

