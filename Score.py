from pygame import *

class Score(Text):
        def __init__(self, pos, baseText = "Stats: ", textSize = 12, textColor=(255,255,255), font = None):
                self.score = 0
                self.baseText = baseText
                self.text = self.baseText + str(self.score)
                Text.__init__(self, pos, self.text, textSize, textColor, font)
                self.change = False
                        
        def setText(self, text):
                self.baseText = text
                self.change = True
                
        def update(self):
                if self.change:
                        self.text = self.baseText + str(self.score)
                        self.image = self.font.render(self.text, 1, self.textColor)
                        self.rect = self.image.get_rect(center = self.rect.center)
                        self.change = False
        
        def setScore(self, score):
                self.score = score
                self.change = True
                
        def increaseScore(self, amount = 1):
                self.score += amount
                self.change = True
                
        def resetScore(self):
                self.score = 0
                self.change = True
