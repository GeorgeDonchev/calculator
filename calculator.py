from tkinter import *


def clear_cmd():
    display.delete(0, END)


def clicked_button(number):
    current_number = display.get()
    display.delete(0, END)
    display.insert(0, str(current_number) + str(number))


def sum_cmd():
    first_number = display.get()
    global f_num, math
    math = 'addition'
    f_num = int(first_number)
    display.delete(0, END)


def subtract():
    first_number = display.get ()
    global f_num, math
    math = 'subtraction'
    f_num = int (first_number)
    display.delete (0, END)


def multiply():
    first_number = display.get ()
    global f_num, math
    math = 'multiply'
    f_num = int (first_number)
    display.delete (0, END)


def divide():
    first_number = display.get ()
    global f_num, math
    math = 'division'
    f_num = int (first_number)
    display.delete (0, END)


def submit():
    second_number = int(display.get())
    display.delete(0, END)
    result = 0
    if math == 'addition':
        result = f_num + second_number
    elif math == 'subtraction':
        result = f_num - second_number
    elif math == 'multiply':
        result = f_num * second_number
    elif math == 'division':
        result = f'{f_num / second_number:.2f}'

    display.insert(0, result)


root = Tk()
root.title('Simple calculator')
# root.geometry("100x350")

display = Entry(root, width = 45, borderwidth = 5)
display.grid(row = 0, column = 0, columnspan = 3)

btn_seven = Button(root, text = '7', padx= 40, pady=20, command = lambda : clicked_button(7))
btn_seven.grid(row = 1, column = 0)

btn_eight = Button(root, text ='8', padx=40, pady=20, command= lambda : clicked_button(8))
btn_eight.grid(row=1, column = 1)

btn_nine = Button(root, text = '9', padx=40, pady=20, command = lambda : clicked_button(9))
btn_nine.grid(row=1, column=2)

btn_four = Button(root, text = '4', padx=40, pady=20, command = lambda : clicked_button(4))
btn_four.grid(row = 2, column = 0)

btn_five = Button(root, text ='5', padx=40, pady=20, command= lambda : clicked_button(5))
btn_five.grid(row=2, column = 1)

btn_six = Button(root, text = '6', padx=40, pady=20, command = lambda : clicked_button(6))
btn_six.grid(row=2, column=2)

btn_one = Button(root, text = '1', padx=40, pady=20, command = lambda : clicked_button(1))
btn_one.grid(row = 3, column = 0)

btn_two = Button(root, text ='2', padx=40, pady=20, command= lambda : clicked_button(2))
btn_two.grid(row=3, column = 1)

btn_three = Button(root, text = '3', padx=40, pady=20, command = lambda : clicked_button(3))
btn_three.grid(row=3, column=2)

btn_zero = Button(root, text = '0', padx=40, pady=20, command = lambda : clicked_button(0))
btn_zero.grid(row = 4, column = 0)

clear_btn = Button(root, text= 'clear',padx=30, pady=20, command = clear_cmd)
clear_btn.grid(row= 5, column = 2)

sum_btn = Button(root, text= '+', padx=40, pady=20, command = sum_cmd)
sum_btn.grid(row=4, column = 1)

submit_btn = Button(root, text= '=', padx=135, pady=20, command = submit, bg = '#48484A', fg = 'White')
submit_btn.grid(row=6, column = 0, columnspan = 3)


subtract_btn = Button(root, text='-', padx=40, pady=20, command = subtract)
subtract_btn.grid(row=4, column = 2)
multiply_btn = Button(root, text='*',padx = 41, pady=20, command = multiply)
multiply_btn.grid(row=5, column = 0)
divide_btn = Button (root, text = '/', padx = 41, pady = 20, command = divide)
divide_btn.grid(row=5, column=1)


root.mainloop()