from tkinter import *

root = Tk()

root.title('Calc')
root.resizable(height=False, width=False)
root.geometry('800x500+500+100')
root.configure(background='#67ACB6')

txt1 = StringVar()
num1 = Entry(textvariable=txt1, bd=4, bg='#5AD05E', font='arial 15')
num1.place(height=65, width=630, y=10, x=150)

sys1Scale = Scale(orient=HORIZONTAL, length=110, from_=2, to=16, tickinterval=14, resolution=1, bg='#67ACB6',
                 font='arial 12 bold', fg='#222222', activebackground='#FFAB00', bd=0, highlightthickness=0)
sys1Scale.place(width=110, y=5, x=15)

txt2 = StringVar()
num2 = Entry(textvariable=txt2, bd=4, bg='#5AD05E', font='arial 15')
num2.place(height=65, width=630, y=90, x=150)

sys2Scale = Scale(orient=HORIZONTAL, length=110, from_=2, to=16, tickinterval=14, resolution=1, bg='#67ACB6',
                 font='arial 12 bold', fg='#222222', activebackground='#FFAB00', bd=0, highlightthickness=0)
sys2Scale.place(width=110, y=90, x=15)

op = StringVar()
op.set(0)
plus = Radiobutton(text='Сложить', variable=op, value=0, activebackground='#67ACB6', bg='#67ACB6',
                   font='arial 12 bold', fg='#222222', overrelief='groove')
minus = Radiobutton(text='Вычесть', variable=op, value=1, activebackground='#67ACB6', bg='#67ACB6',
                    font='arial 12 bold', fg='#222222', overrelief='groove')
mult = Radiobutton(text='Умножить', variable=op, value=2, activebackground='#67ACB6', bg='#67ACB6',
                   font='arial 12 bold', fg='#222222', overrelief='groove')
division = Radiobutton(text='Разделить', variable=op, value=3, activebackground='#67ACB6', bg='#67ACB6',
                       font='arial 12 bold', fg='#222222', overrelief='groove')

plus.place(y=200,x=55)
minus.place(y=230, x=55)
mult.place(y=260, x=55)
division.place(y=290, x=55)

res = StringVar()
result = Entry(textvariable=res, bd=4, bg='#5AD05E', font='arial 15')
result.place(height=65, width=630, y=400, x=150)

resScale = Scale(orient=HORIZONTAL, length=110, from_=2, to=16, tickinterval=14, resolution=1, bg='#67ACB6',
                 font='arial 12 bold', fg='#222222', activebackground='#FFAB00', bd=0, highlightthickness=0)
resScale.place(width=110, y=400, x=15)

btn = Button(text='Вычислить', bg='#DCDCDC', font='Arial 25 bold', activebackground='#DCDCDC', fg='#222222',
             bd=3)
btn.place(height=100, width=200, y=210,x=300)


root.mainloop()