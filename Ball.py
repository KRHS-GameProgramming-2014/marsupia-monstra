import pygame, math

import math,sys,pygame

class Ball():
	def __init__(self,player,image):
		self.facing = player.facing
		if self.facing == "up":
			self.image = pygame.image.load(image)
			self.speed = [0, -5]
		elif self.facing == "down":
			self.image = pygame.image.load(image)
			self.speed = [0, 5]
		elif self.facing == "right":
			self.image = pygame.image.load(image)
			self.speed = [5, 0]
		elif self.facing == "left":
			self.image = pygame.image.load(image)
			self.speed = [-5, 0]
		self.rect = self.image.get_rect()
		self.damage = 10
		self.place(player.rect.center)
		self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
		self.move()
		self.living = True
		distance = 0
		
		
	  
	def move(self):
		self.rect = self.rect.move(self.speed)
	
	def collideWall(self, width, height):
		if self.rect.left < 0 or self.rect.right > width:
			self.living = False
		if self.rect.top < 0 or self.rect.bottom > height:
			self.living = False
	
	def collideEnemy(self, other):
		if self != other:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					self.living = False
										
						
	def place(self, pt):
		self.rect.center = pt
		
	def update(self, width, height):
		self.move()
		self.collideWall(width, height)
		distance += 1
		
		
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[1]
		x2 = pt[0]
		y2 = pt[1]
		return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
		
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += 1
		else:
			self.waitCount = 0
			self.facingChanged = True
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
		
