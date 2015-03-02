import math,pygame
from Base import *
from Ball import *



class Player(Base):
	def __init__(self, pos):
		Base.__init__(self, "Rsc/Player/StationaryDown.png", [0,0], pos)
		self.upImages = [pygame.image.load("Rsc/Player/StationaryUp.png"),
						 pygame.image.load("Rsc/Player/WalkUp1.png"),
						 pygame.image.load("Rsc/Player/StationaryUp.png"),
						 pygame.image.load("Rsc/Player/WalkUp2.png")]
		self.downImages = [pygame.image.load("Rsc/Player/StationaryDown.png"),
						   pygame.image.load("Rsc/Player/WalkDown1.png"),
						   pygame.image.load("Rsc/Player/StationaryDown.png"),
						   pygame.image.load("Rsc/Player/WalkDown2.png")]
		self.leftImages = [pygame.image.load("Rsc/Player/StationaryLeft.png"),
						   pygame.image.load("Rsc/Player/WalkLeft1.png"),
						   pygame.image.load("Rsc/Player/StationaryLeft.png"),
						   pygame.image.load("Rsc/Player/WalkLeft2.png")]
		self.rightImages = [pygame.image.load("Rsc/Player/StationaryRight.png"),
							pygame.image.load("Rsc/Player/WalkRight1.png"),
							pygame.image.load("Rsc/Player/StationaryRight.png"),
							pygame.image.load("Rsc/Player/WalkRight2.png")]
		self.facing = "up"
		self.changed = False
		self.images = self.upImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.15
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 3
		self.throwing = False
		self.ballCount = 0
		self.maxBallCount = 10
		self.ballCoolDown = 0
		self.ballCoolDownMax = 50
		self.balldelay = 5
		

			
	def update(self, width, height):
		Base.update(self, width, height)
		self.animate()
		self.changed = False
		if self.ballCoolDown > 0:
			self.ballCoolDown -=1

		
	def collideWall(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = 0
				self.didBounceX = True
				#print "hit xWall"
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = 0
				self.didBounceY = True
				#print "hit xWall"
	
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += 1
		else:
			self.waitCount = 0
			self.changed = True
			if self.frame < self.maxFrame:
				self.frame += 1
			else:
				self.frame = 0
		
		if self.changed:	
			if self.facing == "up":
				self.images = self.upImages
			elif self.facing == "down":
				self.images = self.downImages
			elif self.facing == "right":
				self.images = self.rightImages
			elif self.facing == "left":
				self.images = self.leftImages
			
			self.image = self.images[self.frame]
			
	def attack(self, atk):
		if atk == "throwing" and self.ballCoolDown == 0:
			self.throwing = True
			self.ballCoolDown = self.ballCoolDownMax
			return [Ball(self,"Rsc/Balls/Pokeball.png")]
		return []
	
	
	def go(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
		elif direction == "down":
			self.facing = "down"
			self.changed = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
			
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0
