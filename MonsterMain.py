from Monster import *
import pygame
pygame.init()
width = 800
height = 600



clock = pygame.time.Clock()
size = width, height

bgColor = r,g,b = 255, 165, 0
screen = pygame.display.set_mode(size)


while True:
	
	
	bgColor = r,g,b
	screen.fill(bgColor)
	pygame.display.flip()
	clock.tick(60)
