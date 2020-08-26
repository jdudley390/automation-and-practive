from tkinter import*
from PIL import ImageTk,Image
root = Tk()

root.title('Learning tkinter')
#iconbitmap creates icon on top left of window
#VS isn't finding my origin folders well so enter as a raw string
root.iconbitmap(r'C:\Users\Jonathan\Pictures\Giannis-Zographos-English-Football-Club-Arsenal-FC.ico')

#adding images is 3 step process
#define image
my_img1 = ImageTk.PhotoImage(Image.open(r'C:\Users\Jonathan\Pictures\DBZ\goku.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open(r'C:\Users\Jonathan\Pictures\DBZ\littlegoku.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open(r'C:\Users\Jonathan\Pictures\DBZ\MRPOPO.png'))


#put each image into a list
img_list = [my_img1, my_img2, my_img3,]

my_label = Label(image=my_img1)
my_label.grid(row=1, column=0, columnspan=3)
#put image into GUI


def fwd(image_number):
    global my_label
    global button_back
    global button_fwd
    #grid_forget is an internal function that can be used to get rid of something 
    #images appear on the my_label so call grid_forget with it
    my_label.grid_forget()
    #because on button_fwd, lambda:fed(2) starts at the third image(0,1,2)
    #2-1 will give you the second image
    my_label = Label(image=img_list[image_number+1])
    button_fwd = Button(root, text = '>>', command=lambda:fwd(image_number+1))
    button_back = Button(root, text = '<<', command=lambda:back(image_number-1))
    #after each button is called to do its job you have to 
    #reput them on the grid

    if image_number == 4:
        button_fwd = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row = 0, column = 0)
    button_fwd.grid(row=0, column=2)
def back(image_number):
    global my_label
    global button_back
    global button_fwd

#create buttons

button_back = Button(root, text = '<<', command=back)
button_exit = Button(root, text = 'Exit', command=root.quit)
button_fwd = Button(root, text = '>>', command=lambda:fwd(0))


button_back.grid(row = 0, column = 0)
button_exit.grid(row=0, column=1)
button_fwd.grid(row=0, column=2)
root.mainloop()


