from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text
    
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text= total
    
    except SyntaxError:
        equation_label.set("Syntax error")

    except ZeroDivisionError:
        equation_label.set("Error")


def clear():
    global equation_text

    equation_label.set('')
    equation_text = ""

def lightMode():
    global light_mode
    light_mode = not lightMode 
    if lightMode:
        window.config(bg="light gray")
        label.config(bg="white", fg="black")
        frame.config(bg="light gray")
        button1.config(bg="light gray", fg="black")
        button1.config(bg="light gray", fg="black")
        button2.config(bg="light gray", fg="black")
        button3.config(bg="light gray", fg="black")
        button4.config(bg="light gray", fg="black")
        button5.config(bg="light gray", fg="black")
        button6.config(bg="light gray", fg="black")
        button7.config(bg="light gray", fg="black")
        button8.config(bg="light gray", fg="black")
        button9.config(bg="light gray", fg="black")
        button0.config(bg="light gray", fg="black")
        plus.config(bg="light gray", fg="black")
        minus.config(bg="light gray", fg="black")
        multiply.config(bg="light gray", fg="black")
        divide.config(bg="light gray", fg="black")
        equal.config(bg="light gray", fg="black")
        decimal.config(bg="light gray", fg="black")
        clear.config(bg="light gray", fg="black")
        darkMode.config(bg="light gray", fg="black")         
        lightMode.config(bg="light gray", fg="black")


def darkMode():
    global dark_mode
    dark_mode = not darkMode
    if darkMode:
        window.config(bg="black")
        label.config(bg="black", fg="white")
        frame.config(bg="black")
        button1.config(bg="black", fg="white")
        button2.config(bg="black", fg="white")
        button3.config(bg="black", fg="white")
        button4.config(bg="black", fg="white")
        button5.config(bg="black", fg="white")
        button6.config(bg="black", fg="white")
        button7.config(bg="black", fg="white")
        button8.config(bg="black", fg="white")
        button9.config(bg="black", fg="white")
        button0.config(bg="black", fg="white")
        plus.config(bg="black", fg="white")
        minus.config(bg="black", fg="white")
        multiply.config(bg="black", fg="white")
        divide.config(bg="black", fg="white")
        equal.config(bg="black", fg="white")
        decimal.config(bg="black", fg="white")
        clear.config(bg="black", fg="white")
        darkMode.config(bg="black", fg="white")
        lightMode.config(bg="black", fg="white")



window = Tk()
window.title("Calculator")
window.geometry("600x600")



equation_text = ""

equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('consolas', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, 
                command=lambda: button_press(1))
button1.grid(row= 0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, 
                command= lambda: button_press(2))
button2.grid(row= 0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, 
                command= lambda: button_press(3))
button3.grid(row= 0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, 
                command= lambda: button_press(4))
button4.grid(row= 1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, 
                command= lambda: button_press(5))
button5.grid(row= 1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, 
                command= lambda: button_press(6))
button6.grid(row= 1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, 
                command= lambda: button_press(7))
button7.grid(row= 2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, 
                command= lambda: button_press(8))
button8.grid(row= 2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, 
                command= lambda: button_press(9))
button9.grid(row= 2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, 
                command= lambda: button_press(0))
button0.grid(row= 3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35, 
                command= lambda: button_press('+'))
plus.grid(row= 0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, 
                command= lambda: button_press('-'))
minus.grid(row= 1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, 
                command= lambda: button_press('*'))
multiply.grid(row= 2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, 
                command= lambda: button_press('/'))
divide.grid(row= 3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35, 
                command= equals)
equal.grid(row= 3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35, 
                command= lambda: button_press('.'))
decimal.grid(row= 3, column=1)

darkMode =Button(frame, text='Dark', height=4, width=9, font=35,
                    command=darkMode)
darkMode.grid(row=0, column=4)

lightMode =Button(frame, text='Light', height=4, width=9, font=35,
                    command=lightMode)
lightMode.grid(row=1, column=4)

clear = Button(window, text='clear', height=4, width=12, font=35, 
                command=clear)
clear.pack()


window.mainloop()