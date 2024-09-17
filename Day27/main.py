from tkinter import *


def button_click():
	my_label.config(text=input.get())


window = Tk()
window.title("My Apps")
window.minsize(width=500,height=300)


# label
my_label = Label(text="I'm a Label",font=("Arial",24,"italic"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=10,y=0)
my_label.grid(column=0,row=0) 

# place pack grid are same but can't use at same program


# button
button = Button(text="click me",command=button_click)
# button.pack()
button.grid(column=1,row=1)

new_button=Button(text="new button")
new_button.grid(column=2,row=0)

# Entry
input = Entry(width=10)
# input.pack()



window.mainloop()