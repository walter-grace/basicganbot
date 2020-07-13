from tkinter import *
from aitextgen import aitextgen

gui = Tk(className='Text GANS')
e = Entry(gui, width=50)
e.pack()

gui.geometry("540x240")

def callBack():
    ai = aitextgen()
    ai.generate(n=3, prompt=e.get(), max_length=210, temperature=1.2)
    myLabel = Label(gui, text="Until I can figure out how to input the gen text here go check your console")
    myLabel.pack()

myButton = Button(gui, text="Enter your phrase, then press here", command=callBack)

myButton.pack()


gui.mainloop()