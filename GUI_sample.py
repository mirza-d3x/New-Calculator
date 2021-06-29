#sample Calculator

from tkinter import *

#Operations
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == 'c':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


window = Tk()
window.geometry("600x650")
window.minsize(600,650)
window.maxsize(600,650)
window.config(bg="grey")
window.title("Calculator By Mirza")

scvalue = StringVar()
scvalue.set("")
f = Frame(window, padx=20, pady=20)
screen = Entry(f, textvar= scvalue, font="luciid 50 bold", bg='light blue')
screen.pack(fill=X, padx=20, pady=15)
f.pack()



