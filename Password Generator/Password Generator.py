from os import startfile
import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


# Creating the main window.
window_1 = Tk()
window_1.title("Password Generator")
window_1.geometry('320x110')
window_1.resizable(width=False, height=False)
lbl = Label(window_1)
lbl.grid(column=0, row=0)


# Symbols.
lower_letters = ("abcdefghijklmnopqrstuvwxyz")
upper_letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = ("0123456789")
symbols = ('!"#$%&()*+,-./:;<=>?@[\\]~`_^{|}')
all_symbols = lower_letters + upper_letters + numbers + symbols


# Function with text symbols.
def label(TEXT, X, Y):
    lbl = Label(window_1, text=TEXT, font=("Arial Bold", 10))
    lbl.grid(column=0, row=0)
    lbl.place(x=X, y=Y)


# The button for calculating indicators.
def button(TEXT, com, X, Y):
    btn1 = Button(window_1, text=TEXT, command=com)
    btn1.grid(column=0, row=0)
    btn1.place(x=X, y=Y)


# Text designations.
label('КОЛЛ-ВО СИМВОЛОВ(до 30 шт.):', 10, 10)
label('ПАРОЛЬ:', 10, 40)


# Input field.
txt1 = Entry(window_1, width=10)
txt1.grid(column=0, row=0)
txt1.place(x=225, y=10)


# Password generation.
def generate():
    value = txt1.get()
    global password
    length = int(value)
    password = "".join(random.sample(all_symbols, length))
    label(password, 75, 40)


# Copying the password to the clipboard.
def copy_pass():
    pyperclip.copy(password)


# Calling buttons.
button('СГЕНЕРИРОВАТЬ', generate, 10, 70)
button('СКОПИРОВАТЬ', copy_pass, 120, 70)


window_1.mainloop()
