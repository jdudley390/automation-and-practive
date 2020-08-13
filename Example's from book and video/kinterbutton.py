from tkinter import * 

root = Tk()

def myClick():
    myLabel1 = Label(root, text='Look! I clicked a button')
    myLabel1.pack()

#Create a button widget
#can use state=Disable to make a button not click or function
#padx and pady control size
#use command to make button function. clicking it will call the function
#command from function myClick will cause "Look! I clicked a button to appear everytime you click the button
#bg and fg change the color of buttons
myButton =Button(root, text='Click Me', command=myClick, fg='red', bg='black')
myButton.pack()

root.mainloop()
