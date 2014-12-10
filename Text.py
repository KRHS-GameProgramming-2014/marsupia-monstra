from Tkinter import *
from pygame import *
root = Tk()

	
	
text1 = Text(root, height=20, width=35)
photo= pygame.image.load('marsupiamonstra.png')
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
