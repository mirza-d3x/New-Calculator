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



#This function will handle the button click
def buttonClickHandler(buttonText):
    screenText=screen.get()
    #if button ± is clicked then multiply the value will-
    if buttonText == '±':
        screenText = str(-(float(screenText)))
        #setting result to screen
        return
    #if button sqrt is click then finds square root of number in screen and set result back to screen
    if buttonText == '√':
        screenText = str(math.sqrt(float(screenText)))
        screen.set(screenText)
        return
    #if operator is already present at last of text on screen then it will do nothing
    if buttonText in ['+', '-', 'X', '÷']:
        return

    #if user tried to type 2 dots
    screenText=screenText.replace('..', '.')

    screenText=screenText + buttonText
    screenText.set(screenText)

def main():
    #get text from screen
    screenText=screen.get()
    screen.set('')
    #replaced x with * and ÷ with / inorder to easily pass to aval function
    screenText=screenText.replace('X', '*')
    screenText=screenText.replace('÷', '/')
    try:
        #generating result
        answer=round(eval(screenText),2)
    except:
        #if any errorr occurs
        answer="Error"
    #setting text to screen
    screen.set(str(answer))
