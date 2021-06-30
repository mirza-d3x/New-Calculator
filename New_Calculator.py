from tkinter import *
import math
root = Tk()
root.title("CALCULATOR")
root.geometry("420x530")
root.configure(bg = "lightblue")

screen = StringVar()
screen.set('')


# removes the last character of text on screen
def clearScreenByOne():
    screenText = screen.get()
    screen.set(screenText[:-1])

# clear all screen
def clearScreen():
    screen.set(' ')

#This function will handle the button click
def buttonClickHandler(buttonText):
    screenText=screen.get()
    #if button ± is clicked then multiply the value will -
    if buttonText == '±':
        screenText = str(-(float(screenText)))
        #setting result to screen
        screen.set(screenText)
        return
    #if button sqrt is click then finds squre root of number in screen and set result back to screen
    if buttonText == '√':
        screenText = str(math.sqrt(float(screenText)))
        screen.set(screenText)
        return
    #if operator is already present at last of text on screen then it will do nothing
    if buttonText in ['+','-','x','÷'] and  screenText[-1] in ['+','-','x','÷']:
        return

    #if user tried to type 2 dots
    screenText = screenText.replace('..','.')

    screenText = screenText + buttonText
    screen.set(screenText)


def main():
    #get text from screen
    screenText = screen.get()
    screen.set(' ')
    #replaced x wit * and ÷ with / inorder to easily pass to aval function
    screenText = screenText.replace('x', '*')
    screenText = screenText.replace('÷', '/')
    try:
        #generating result
        answer = round(eval(screenText),2)
    except:
        #if any errorr occurs
        answer = "Error"
    #setting text to screen
    screen.set(str(answer))

def run():
    #generates label on window to show output
    lbl_outputScreen = Label(root,text="",bg="white",width=18,height=2,font=('Arial','30'),textvariable=screen, anchor='se')
    #placing label on screen on row 0 col 0 means on top and giving it space of 4 solumns to file entire width
    lbl_outputScreen.grid(row=0,column=0,columnspan=4)

    #below generates buttons in form of grid which will call button_clickhandler method when clicked
    btn_clearScreenByOne = Button(root,text="➜",bg="lightgrey",fg="black",width = 3,height=1,font=('Arial','25'),command=clearScreenByOne)
    btn_plus_minus = Button(root,text="±",bg="lightgrey",fg="black",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('+-'))
    btn_sqrt = Button(root,text="√",bg="lightgrey",fg="black",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('√'))
    btn_mul = Button(root,bg="orange",fg="black",text="x",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('x'))
    btn_clearScreenByOne.grid(row=1,column=1,pady=10)
    btn_plus_minus.grid(row=1,column=2,pady=10)
    btn_sqrt.grid(row=1,column=3,pady=10)
    btn_mul.grid(row=3,column=3,pady=10)

    #second row
    btn7 = Button(root,bg="grey",fg="black",text="7",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('7'))
    btn8 = Button(root,bg="grey",fg="black",text="8",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('8'))
    btn9 = Button(root,bg="grey",fg="black",text="9",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('9'))
    btn_divide = Button(root,bg="orange",fg="black",text="÷",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('÷'))
    btn7.grid(row=2,column=0,pady=10)
    btn8.grid(row=2,column=1,pady=10)
    btn9.grid(row=2,column=2,pady=10)
    btn_divide.grid(row=2,column=3,pady=10)

    # The third row
    btn4 = Button(root,bg="grey",fg="black",text="4",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('4'))
    btn5 = Button(root,bg="grey",fg="black",text="5",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('5'))
    btn6 = Button(root,bg="grey",fg="black",text="6",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('6'))
    btn_minus = Button(root,bg="orange",fg="black",text="-",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('-'))
    btn4.grid(row=3,column=0,pady=10)
    btn5.grid(row=3,column=1,pady=10)
    btn6.grid(row=3,column=2,pady=10)
    btn_minus.grid(row=4,column=3,pady=10)

    # Fourth row
    btn1 = Button(root,bg="grey",fg="black",text="1",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('1'))
    btn2 = Button(root,bg="grey",fg="black",text="2",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('2'))
    btn3 = Button(root,bg="grey",fg="black",text="3",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('3'))
    btn_add = Button(root,bg="orange",fg="black",text="+",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('+'))
    btn1.grid(row=4,column=0,pady=10)
    btn2.grid(row=4,column=1,pady=10)
    btn3.grid(row=4,column=2,pady=10)
    btn_add.grid(row=5,column=3,pady=10)

    # The fifth row
    btn0 = Button(root,bg="grey",fg="black",text="0",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('0'))
    btn_dot = Button(root,bg="grey",fg="black",text=".",width = 3,height=1,font=('Arial','25'),command=lambda: buttonClickHandler('.'))
    btn_equal = Button(root,bg="orange",fg="black",text="=",width = 3,height=1,font=('Arial','25'),command=main)
    btn_clear = Button(root,text="C",bg = "red",fg = "black",width = 3,height=1,font=('Arial','25'),command=clearScreen)
    btn_clear.grid(row=1,column=0,pady=10)
    btn0.grid(row=5,column=0,pady=10)
    btn_dot.grid(row=5,column=1,pady=10)
    btn_equal.grid(row=5,column=2,pady=10)
#calling run method
run()
#showing window until user don't closes it
root.mainloop()