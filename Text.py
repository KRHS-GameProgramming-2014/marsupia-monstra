import pygame

class Text():
        def __init__(self, pos, text = "", textSize = 12, textColor=(255,255,255), font = None):
                self.text = text
                self.textColor = textColor
                self.font = pygame.font.Font(font, textSize)
                self.image = self.font.render(self.text, 1, textColor)
                self.rect = self.image.get_rect()
                self.place(pos)
                
        def place(self, pos):
                self.rect.center = pos
                
        def setText(self, text):
                self.text = text
                self.image = self.font.render(text, 1, textColor)
                self.rect = self.image.get_rect(center = self.rect.center)
                
        def update(self, width, height):
                pass

