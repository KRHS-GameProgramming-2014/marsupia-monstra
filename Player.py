import math,pygame
from Base import *
from Ball import *



class Player(Base):
	def __init__(self, pos):
		Base.__init__(self, "Rsc/Player/StationaryDown.png", [0,0], pos)
		self.upImages = [pygame.image.load("Rsc/Player/WalkUp1.png"),
						 pygame.image.load("Rsc/Player/WalkUp2.png")]
		self.downImages = [pygame.image.load("Rsc/Player/WalkDown1.png"),
						   pygame.image.load("Rsc/Player/WalkDown2.png")]
		self.leftImages = [pygame.image.load("Rsc/Player/StationaryLeft.png"),
						   pygame.image.load("Rsc/Player/WalkLeft2.png")]
		self.rightImages = [pygame.image.load("Rsc/Player/StationaryRight.png"),
							pygame.image.load("Rsc/Player/WalkRight2.png")]
		self.facing = "up"
		self.changed = False
		self.images = self.upImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.135
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 2
		self.throwing = False
		self.ballCount = 0
		self.maxBallCount = 10
		self.ballCoolDown = 0
		self.ballCoolDownMax = 15
		self.balldelay = 5
		self.health = 12 
		self.maxHurtDelay = 30 * 3
		self.hurtDelay = 0
		self.invincible = False
		self.living = True
		self.moving = False

			
	def update(self, width, height):
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
		self.animate()
		self.changed = False
		if self.ballCoolDown > 0:
			self.ballCoolDown -=1
		if self.hurtDelay > 0:
			self.hurtDelay -= 1
		else:
			self.invincible = False
			
	def move(self):
		self.rect = self.rect.move(self.speed)
			
	def collideWall(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = -self.speedx
				self.update(width, height)
				self.speedx = 0
				#print "hit xWall"
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = -self.speedy
				self.update(width, height)
				self.speedy = 0
				#print "hit xWall"
	
	def collideEnemy(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if self.invincible == False:
						self.hurt()
	
	def hurt(self, amount=1):
		self.changed = True
		self.hurting = True
		if not self.invincible:
			self.health -= amount
			print self.health
			self.invincible = True
			self.hurtDelay = self.maxHurtDelay
			
		if self.health <= 0:
			self.living = False
	
	def animate(self):
		if self.moving:
			if self.waitCount < self.maxWait:
				self.waitCount += 1
			else:
				self.waitCount = 0
				self.changed = True
				if self.frame < self.maxFrame:
					self.frame += 1
				else:
					self.frame = 0
		else:
			self.waitCount = self.maxWait
			
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
			self.moving = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
			self.moving = False
		elif direction == "down":
			self.facing = "down"
			self.changed = True
			self.moving = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
			self.moving = False
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.moving = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
			self.moving = False
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.moving = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0
			self.moving = False


