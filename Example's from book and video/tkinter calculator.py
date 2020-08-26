from tkinter import *
import math

root = Tk()
#.title changes the top bars name. i.e. firefox, winamp etc.
root.title('Calculator')

e = Entry(root, width=35, borderwidth=5)
#the function button add will be called when button1 is clicked
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #e.delete(0, END)
    #create a variable that will be what is currently in the text/number field
    current = e.get()
    #delete what is in the field so if you type '1' than '5' you don't get "151'
    e.delete(0, END)
    #because we are using integers call the str function so the numbers are not added together
    #simply put in the text/number field together
    e.insert(0, str(current) + str(number))

def clear():
    e.delete(0, END)

def equal():
    second_number = e.get()
    e.delete(0, END)
    #make sure 2nd number is int
    #don't need a global only button_equal will need to use it
    if Tmath == 'addition':
        e.insert(0, f_num + int(second_number))
    elif Tmath =='subtraction':
        e.insert(0, f_num - int(second_number))
    elif Tmath == 'multiplication':
        e.insert(0, f_num * int(second_number))
    elif Tmath == 'division':
        e.insert(0, f_num / int(second_number))
    elif Tmath == 'exponent':
        e.insert(0, f_num ** int(second_number))

#create function to get first integer entered
def add():
    first_number = e.get()
    #saving int as global allows it to be used be the equal function to get the first number to add to the second
    global f_num
    #create global math variable
    global Tmath
    Tmath = 'addition'
    f_num = int(first_number)
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global f_num
    global Tmath
    Tmath = 'subtraction'
    f_num = int(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num
    global Tmath
    Tmath = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)
def divide():
    first_number = e.get()
    global f_num
    global Tmath
    Tmath = 'division'
    f_num = int(first_number)
    e.delete(0, END)

def exponent():
    first_number = e.get()
    global f_num
    global Tmath
    Tmath = 'exponent'
    f_num = int(first_number)
    e.delete(0, END)
def squareRoot():
    first_number = e.get()
    global f_num
    global Tmath
    Tmath = 'square root'
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0, math.sqrt(f_num))


    

#create number buttons
#when calling a function with tkinter(all GUI?) do not need to add "()" at the end
button1 = Button(root, text='1', padx=35, pady=19, command=lambda:button_click(1))
button2 = Button(root, text='2', padx=35, pady=19, command=lambda:button_click(2))
button3 = Button(root, text='3', padx=35, pady=19, command=lambda:button_click(3))
button4 = Button(root, text='4', padx=35, pady=19, command=lambda:button_click(4))
button5 = Button(root, text='5', padx=35, pady=19, command=lambda:button_click(5))
button6 = Button(root, text='6', padx=35, pady=19, command=lambda:button_click(6))
button7 = Button(root, text='7', padx=35, pady=19, command=lambda:button_click(7))
button8 = Button(root, text='8', padx=35, pady=19, command=lambda:button_click(8))
button9 = Button(root, text='9', padx=35, pady=19, command=lambda:button_click(9))
button0 = Button(root, text='0', padx=35, pady=19, command=lambda:button_click(0))
#operator buttons
#when calling a function with tkinter(all GUI?) do not need to add "()" at the end
clearButton = Button(root, text='C', padx=77, pady=19, command=clear)
equalsButton =Button(root, text='=', padx=77, pady=19, command=equal)
addButton = Button(root, text='+', padx=34, pady=19, command=add)
subtractButton = Button(root, text='-', padx=35, pady=19, command=subtract)
multiplyButton = Button(root, text='*', padx=35, pady=19, command=multiply)
divideButton = Button(root, text='/', padx=36, pady=19, command=divide)
exponentButton = Button(root, text='^', padx=35, pady = 19, command=exponent)
sqrtButton = Button(root, text = '√', padx=35, pady = 19, command=squareRoot)
#place buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)




button0.grid(row=4, column=0)
clearButton.grid(row=4, column=1, columnspan=2)

addButton.grid(row=5, column=0)
equalsButton.grid(row=5, column=1, columnspan=2)

subtractButton.grid(row=6, column=0)
multiplyButton.grid(row=6, column=1)
divideButton.grid(row=6, column=2)

exponentButton.grid(row=7, column=0)
sqrtButton.grid(row=7, column=1)
root.mainloop()
