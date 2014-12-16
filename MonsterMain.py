from Monster import *
import pygame


pygame.init()

clock = pygame.time.Clock()

width = 1080 
height = 720
size = width, height

bgColor = r,g,b = 255, 165, 0
screen = pygame.display.set_mode(size)

Kangaroo=Monster("rsc/marsupiamonstra.png", 1, 1, 1, 10, 0, 0, [500,400], "lightning")

while True:
	
	
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(Kangaroo.image, Kangaroo.rect)
	pygame.display.flip()
	clock.tick(60)
