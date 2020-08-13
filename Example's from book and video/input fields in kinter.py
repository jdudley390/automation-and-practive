from tkinter import *

root = Tk()
#create entry widget
#entry widget allows text fields
e = Entry(root)
e.pack()
#insert function adds text inside the text field
e.insert(0, "Enter your name")
#.get function goes and gets the text you've typed
#e.get()
#padx and pady give a border around a text field
def myClick():
    hello = 'Hello ' + e.get()
    myLabel1 = Label(root, text=hello)
    myLabel1.pack()

myButton =Button(root, text='Enter your name', command=myClick)
myButton.pack()

root.mainloop()
