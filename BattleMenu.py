from Tkinter import *

def attack():
   filewin = Toplevel(root)
   button = Button(filewin, text="You Attacked!")
   button.pack()
   
def switchMonster():
   filewin = Toplevel(root)
   button = Button(filewin, text="You Switched Monsters!")
   button.pack()
   
def useItem():
  filewin = Toplevel(root)
  button = Button(filewin, text="You used Item!")
  button.pack()


   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Tackle", command=attack)
filemenu.add_command(label="Water Gun", command=attack)
filemenu.add_command(label="Withdraw", command=attack)
filemenu.add_command(label="Tail Whip", command=attack)
menubar.add_cascade(label="Attack", menu=filemenu)

monstermenu = Menu(menubar, tearoff=0)
monstermenu.add_command(label="Monster1", command=switchMonster)
monstermenu.add_command(label="Monster2", command=switchMonster)
monstermenu.add_command(label="Monster3", command=switchMonster)
monstermenu.add_command(label="Monster4", command=switchMonster)
monstermenu.add_command(label="Monster5", command=switchMonster)
monstermenu.add_command(label="Monster6", command=switchMonster)
menubar.add_cascade(label="Monsters", menu=monstermenu)

itemmenu = Menu(menubar, tearoff=0)
itemmenu.add_command(label="Health Potion", command=useItem)
itemmenu.add_command(label="Small Pouch", command=useItem)
menubar.add_cascade(label="Pouch", menu=itemmenu)


