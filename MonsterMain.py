from Monster import *
from Button import *
from Player import *
from Ball import Ball
from Base import Base
import pygame, sys, random
pygame.init()
width = 800
height = 600

#tedst

enemyCounter = 0

size = width, height
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
bgImage = pygame.image.load("RSC/Screens/Start Screen.png").convert()
bgRect = bgImage.get_rect()

balls = []
enemies = []

startButton = Button([width/2, height-300], 
					 "Rsc/Buttons/Start Base.png", 
					 "Rsc/Buttons/Start Clicked.png")
		
character = Player([100,100])
					 
startCharacter = pygame.image.load("RSC/Screens/Start Screen.png",
									"RSC/Screens/Start Screen.png")


clock = pygame.time.Clock()
bgColor = r,g,b = 100, 255, 80
background = pygame.image.load("Rsc/Screens/Final Background.png")
backgroundRect = background.get_rect()
running = False

while True:
	while not running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					running = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				startButton.click(event.pos)
			if event.type == pygame.MOUSEBUTTONUP:
				if startButton.release(event.pos):
					characterLiving = True
					
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(startButton.image, startButton.rect)
		pygame.display.flip()
		clock.tick(60)
		
		
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					character.go("stop left")
					character.go("stop right")
					character.go("stop down")
					character.go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					character.go("stop left")
					character.go("stop down")
					character.go("stop up")
					character.go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					character.go("stop right")
					character.go("stop up")
					character.go("stop left")
					character.go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					character.go("stop right")
					character.go("stop up")
					character.go("stop down")
					character.go("left")
				if event.key == pygame.K_SPACE:
					balls += character.attack("throwing")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					character.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					character.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					character.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					character.go("stop left")
				if event.key == pygame.K_SPACE:
					character.attack("stop throwing")

		
		enemyCounter += 1
		if enemyCounter >= 30 and len(enemies) < 20:
			if randint(0,1) == 1:
				enemies += [Base("Rsc/Monsters/Broku.png", [0,0], [randint(50,250),randint(100,500)])]
				enemyCounter = 0
			else:
				enemies += [Base("Rsc/Monsters/Broku.png", [0,0], [randint(550,750),randint(100,500)])]
				enemyCounter = 0
		
		
		
		character.update(width, height)
		for ball in balls:
			ball.update(width, height)
		for enemy in enemies:
			enemy.update(width, height, character)
		
		for enemy in enemies:
			character.collideEnemy(enemy)
			enemy.collidePlayer(character)
			for ball in balls:
				enemy.collideBall(ball)
				if ball.collideEnemy(enemy):
					balls.remove(ball)

		
		
		
		for ball in balls:
			if not ball.living:
				balls.remove(ball)
		for enemy in enemies:
			if not enemy.living:
				enemies.remove(enemy)		
	
		bgColor = r,g,b
		screen.blit(background, backgroundRect)
		screen.blit(character.image, character.rect)
		for ball in balls:
			screen.blit(ball.image, ball.rect)
			
		for enemy in enemies:
			screen.blit(enemy.image, enemy.rect)	
		
		pygame.display.flip()
		clock.tick(60)
