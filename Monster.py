class Monster():
	def __init__(self, image, attack, defence, speed, maxhp, exp, attribute):
		self.image = pygame.image.load(image)

	def place(self):
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
	def stats(attack, defence, speed, maxhp, hp, exp):
		print "stats"
