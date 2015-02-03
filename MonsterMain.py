from Monster import *
from Button import *
from Player import *
import pygame, sys, random
pygame.init()
width = 800
height = 600


size = width, height
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
bgImage = pygame.image.load("RSC/Screens/Start Screen.png").convert()
bgRect = bgImage.get_rect()

startButton = Button([width/2, height-300], 
				     "Rsc/Buttons/Start Base.png", 
				     "Rsc/Buttons/Start Clicked.png")
		
character = Player([100,100])
				     
startCharacter = pygame.image.load("RSC/Screens/Start Screen.png",
									"RSC/Screens/Start Screen.png")


clock = pygame.time.Clock()
bgColor = r,g,b = 100, 255, 80
background = pygame.image.load("Rsc/Background.png")
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
					running = True
					
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
					character.go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					character.go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					character.go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					character.go("left")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					character.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					character.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					character.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					character.go("stop left")

	
		bgColor = r,g,b
		screen.blit(background, backgroundRect)
		screen.blit(character.image, character.rect)
		character.update(width, height)
		pygame.display.flip()
		clock.tick(60)
