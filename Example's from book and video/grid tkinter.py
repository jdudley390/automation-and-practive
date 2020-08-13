from tkinter import * #"import *" imports everything from module
#Everything in tkinter is a widget

#must have root
root = Tk() #uses the root widget which creates the window

#create a label widget
myLabel1 = Label(root, text ='Hello World')
myLabel2 = Label(root, text ='My name is my name')
myLabel2 = Label(root, text ='My name is my name')

#use grid to put stuff on GUI
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
root.mainloop()
#remember mainloop means the exeution of the program halts
#methos like update_idletasks and update do not block 
#execution continues after those methods finish 