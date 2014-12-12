<<<<<<< HEAD
from Tkinter import *

root = Tk()

	
text1 = Text(root, height=20, width=35)
photo=PhotoImage(file='marsupimonstra.png')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)


text2 = Text(root, height=20, width=35)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 16, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 20, 'bold'))
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 16, 'bold'))
text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Danny Laughlin and Ben Nebwern "))
text2.insert(END,'\nMarsupia Monstra\n', 'big')
quote = """
Play

Settings

Exit

"""
text2.insert(END, quote, 'color')
text2.insert(END, 'Created By\n', 'follow')
text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

root.mainloop()
=======
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
>>>>>>> origin/master
