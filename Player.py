import math,pygame

class Player():
	def __init__(self, pos):
		Player.__init__(self, "Rsc/Player/StationaryDown.png", [0,0], pos)
		self.upImages = [pygame.image.load("Rsc/Player/StationaryDown.png"),
						 pygame.image.load("Rsc/Player/WalkUp1.png"),
						 pygame.image.load("Rsc/Player/WalkUp2.png")]
		self.downImages = [pygame.image.load("Rsc/Player/StationaryUp.png"),
						   pygame.image.load("Rsc/Player/WalkDown1.png"),
						   pygame.image.load("Rsc/Player/WalkDown2.png")]
		self.leftImages = [pygame.image.load("Rsc/Player/StationaryLeft.png"),
						   pygame.image.load("Rsc/Player/WalkLeft1.png"),
						   pygame.image.load("Rsc/Player/WalkLeft2.png")]
		self.rightImages = [pygame.image.load("Rsc/Player/StationaryRight.png"),
						    pygame.image.load("Rsc/Player/WalkRight1.png"),
						    pygame.image.load("Rsc/Player/WalkRight2.png")]


	def canmove(self, direction):
		if direction == "up":
			pos = (int(self.x),int(self.y-1))
		elif direction == "down":
			pos = (int(self.x),int(self.y+1))
		elif direction == "left":
			pos = (int(self.x-1),int(self.y))
		elif direction == "right":
			pos = (int(self.x+1),int(self.y))
		else: return False
