from tkinter import *
import math
window = TK()
window.title("Mirza's Calculator")
window.geometry("420x530")
window.configure(bg="lightblue")

screen=StringVar()
screen.set('')

#clear BUttons
#last charecter Clear
def clearScreenByOne():
    screen.text=screen.get()
    screen.set(screenText[:-1])

#clear Full Charecter
def clearScreen():
    screen.set('')
