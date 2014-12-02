class Monster():
	def __init__(self, image, attack, defence, speed, maxhp, exp, attribute):
		self.image = pygame.image.load(image)

	def place(self, pos= [0,0]):
		self.rect.center = pos
	
