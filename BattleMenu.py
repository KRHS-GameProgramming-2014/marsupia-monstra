from Tkinter import *

def attack():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def switchMonster():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()


   
root = Tk(PlayerMonster, EnemyMonster)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Tackle", command=attack)
filemenu.add_command(label="Water Gun", command=attack)
filemenu.add_command(label="Withdraw", command=attack)
filemenu.add_command(label="Tail Whip", command=attack)
menubar.add_cascade(label="Attack", menu=filemenu)

monstermenu = Menu(menubar, tearoff=0)
monstermenu.add_command(label="Items", command=donothing)
monstermenu.add_command(label="Monsters", command=switchMonster)
menubar.add_cascade(label="Pouch", menu=monstermenu)


root.config(menu=menubar)
root.mainloop()
