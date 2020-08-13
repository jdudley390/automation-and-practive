from tkinter import * #"import *" imports everything from module
#Everything in tkinter is a widget

#must have root
root = Tk() #uses the root widget which creates the window

#create a label widget
myLabel = Label(root, text = 'Hello World')

#pack() packs a widget(myLabel) into the parent widget(root)
#displays it to screen
myLabel.pack()

root.mainloop()
#remember mainloop means the exeution of the program halts
#methos like update_idletasks and update do not block 
#execution continues after those methods finish