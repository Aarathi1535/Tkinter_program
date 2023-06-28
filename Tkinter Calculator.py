from tkinter import *
expression = " "

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
def clear():
    global expression
    expression = " "
    equation.set(" ")
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression =" "
    except:
        equation.set("Error")
        expression = " "

w = Tk()
w.title("I am a Calculator")
w.geometry("1000x6000")
equation = StringVar()
entry_field = Entry(w,textvariable = equation).grid(columnspan = 4 , ipadx = 60)
b1 = Button(w,text = '1',fg = 'black', bg = 'white',command = lambda: press(1) , height =1 , width =7)
b1.grid(row=2,column=0)
b2 = Button(w, text='2', fg='black', bg='white', command=lambda: press(2), height=1, width=7)
b2.grid(row=2, column=1)
b3 = Button(w, text='3', fg='black', bg='white', command=lambda: press(3), height=1, width=7)
b3.grid(row=2, column=2)
b4 = Button(w, text='4', fg='black', bg='white', command=lambda: press(4), height=1, width=7)
b4.grid(row=3, column=0)
b5 = Button(w, text='5', fg='black', bg='white', command=lambda: press(5), height=1, width=7)
b5.grid(row=3, column=1)
b6 = Button(w, text='6', fg='black', bg='white', command=lambda: press(6), height=1, width=7)
b6.grid(row=3, column=2)
b7 = Button(w, text='7', fg='black', bg='white', command=lambda: press(7), height=1, width=7)
b7.grid(row=4, column=0)
b8 = Button(w, text='8', fg='black', bg='white', command=lambda: press(8), height=1, width=7)
b8.grid(row=4, column=1)
b9 = Button(w, text='9', fg='black', bg='white', command=lambda: press(9), height=1, width=7)
b9.grid(row=4, column=2)
b0 = Button(w, text='0', fg='black', bg='white', command=lambda: press(0), height=1, width=7)
b0.grid(row=5, column=0)
bplus = Button(w, text='+', fg='black', bg='white', command=lambda: press('+'), height=1, width=7)
bplus.grid(row=2, column=3)
bminus = Button(w, text='-', fg='black', bg='white', command=lambda: press('-'), height=1, width=7)
bminus.grid(row=3, column=3)
bmul = Button(w, text='*', fg='black', bg='white', command=lambda: press('*'), height=1, width=7)
bmul.grid(row=4, column=3)
bdiv = Button(w, text='/', fg='black', bg='white', command=lambda: press('/'), height=1, width=7)
bdiv.grid(row=5, column=3)
b_equal = Button(w, text='=', fg='black', bg='white', command=equalpress, height=1, width=7)
b_equal.grid(row=5, column=2)
b_clear = Button(w, text='Clear', fg='black', bg='white', command= clear, height=1, width=7)
b_clear.grid(row=5, column=1)
b_dec = Button(w, text='.', fg='black', bg='white', command=lambda: press('.'), height=1, width=7)
b_dec.grid(row=6, column=0)
bb1 = Button(w, text=' ', fg='black', bg='white', command=lambda: press(' '), height=1, width=7)
bb1.grid(row=6, column=1)
bb2 = Button(w, text=' ', fg='black', bg='white', command=lambda: press(' '), height=1, width=7)
bb2.grid(row=6, column=2)
bb3 = Button(w, text=' ', fg='black', bg='white', command=lambda: press(' '), height=1, width=7)
bb3.grid(row=6, column=3)
w.mainloop()