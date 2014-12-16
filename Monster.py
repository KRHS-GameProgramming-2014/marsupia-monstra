import pygame


class Monster():
	def __init__(self, image, attack, defence, speed, maxhp, exp, owner, pos = [0,0], attribute=""):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.place(pos)
	def place(self, pos):
		self.rect.center = pos
	def attacks(attribute):
		moves = ['simple slap']
		if attribute == 'rock':
			moves += 'pompous pebble'
		if attribute == 'lightning':
			moves += 'bearable bolt'
		if attribute == 'fire':
			moves += 'fading flame'
		if attribute == 'wind':
			moves += 'benign breeze'
		if attribute == 'water':
			moves += 'petty precipitation'
	def statistics(attack, defence, speed, maxhp, hp, exp, owner):
		stats = {}
		if owner == 0:
			stats = {attack,
					defence,
					speed,
					maxhp,
					hp,
					exp}
		if owner == 1:
			stats = {maxhp,
					hp}
