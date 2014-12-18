import pygame

pygame.init()

red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

size = width, height = 340,240	
screen = pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = menu(screen, [
						'Marsupia Monstra'
                        'Start Game',
                        'Options',
                        'Quit Game'], 64,64,None,32,1.4,green,red)

if choose == 0:
    print "You choose 'Start Game'."
elif choose == 1:
    print "You choose 'Options'."
elif choose == 2:
    print "You choose 'Quit Game'."
pygame.quit()
exit()
