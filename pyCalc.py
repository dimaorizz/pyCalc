from tkinter import *
from tkinter import messagebox as mb


def check(num, sys):
    alf = '0123456789ABCDEF'
    minuses = 0
    minusesIn = 0

    if len(num) == 0:
        return False
    if num[0] == '-':
        minuses = 1

    for el in num:
        if el.upper() not in alf[:sys]:
            if el == '-':
                minusesIn += 1
                continue
            return False

    if minuses != minusesIn:
        return False
    return True


def any_to_decimal(user_in, basis_of_input):
    minus_flag = 0
    if user_in[0] == '-':
        minus_flag += 1
        user_in = user_in[1:]
    size = list()
    for k in range(len(user_in)-1, -1, -1):
        size.append(k)
    decimal = 0
    i = 0

    for el in user_in:
        if el.upper() == 'A':
            el = 10
        elif el.upper() == 'B':
            el = 11
        elif el.upper() == 'C':
            el = 12
        elif el.upper() == 'D':
            el = 13
        elif el.upper() == 'E':
            el = 14
        elif el.upper() == 'F':
            el = 15

        decimal += int(el) * basis_of_input**size[i]
        i += 1
    if minus_flag == 1:
        decimal = int('-' + str(decimal))
    return decimal


def decimal_to_any(in_decimal, basis_of_output):
    result = list()
    minus_flag = 0
    in_decimal = str(in_decimal)

    if in_decimal[0] == '-':
        minus_flag += 1

    in_decimal = abs(int(in_decimal))

    if in_decimal == 0:
        return '0'

    while in_decimal >= 1:

        temp = in_decimal % basis_of_output

        if temp == 10:
            result.append('A')
        elif temp == 11:
            result.append('B')
        elif temp == 12:
            result.append('C')
        elif temp == 13:
            result.append('D')
        elif temp == 14:
            result.append('E')
        elif temp == 15:
            result.append('F')
        else:
            result.append(str(temp))

        in_decimal //= basis_of_output  # деление на 2 нацело

    result.reverse()
    answer = ''.join(result)  # соединяет элементы списка answer в строку, используя заданный сепаратор ('')

    if minus_flag == 1:
        answer = '-' + answer

    return answer


def dir_to_bin(direct):
    flag = 0 # флаг знака
    i = 0 # счетчик для создания среза
    if direct[0] == '1':
        flag = 1    #флаг 1 если первая цифра 1 в прямом коде

    # считает сколько надо срезать до первой еденицы
    for el in direct[1:]:
        i += 1
        if el == '1':
            break

    if flag == 1:
        return '-' + direct[i:] #если флаг 1 добавляем знак минус к двоичному числу
    else:
        return direct[i:]


def to_direct (bin, digits):
    direct = list()
    i = 1

    if bin[0] == '-':
        while i < digits - len(bin) + 1:
            direct.append('0')
            i += 1
        direct = ''.join(direct)
        direct = '1' + direct + bin[1:]
    else:
        while i < digits - len(bin):
            direct.append('0')
            i += 1
        direct = ''.join(direct)
        direct = '0' + direct + bin

    return direct


def to_reversed (direct):
    reversed = list()

    if direct[0] == '1':
        reversed.append('1')

        for el in direct[1:]:
            if el == '0':
                reversed.append('1')
            elif el == '1':
                reversed.append('0')
        reversed = ''.join(reversed)
        return reversed
    elif direct[0] == '0':
        return direct


def addictional (in_reverse):
    i = 1
    result = list()
    if in_reverse[0] == '1':
        while i <= len(in_reverse):
            if int(in_reverse[-i]) + 1 == 2:
                result.append('0')
                i += 1
            elif int(in_reverse[-i]) + 1 == 1:
                result.append('1')
                i += 1
                break
        if i < len(in_reverse):
            for el in range(len(in_reverse) - i + 1):
                result.append(in_reverse[-i])
                i += 1
        result.reverse()

        return ''.join(result)
    else:
        return in_reverse

def addictonal_sum (num_add1, num_add2):
    temp1 = num_add1
    temp2 = num_add2
    res = list()
    length = len(num_add1)

    flag_trans = 0

    for i in range(length - 1, -1, -1):
        if int(num_add1[i]) + int(num_add2[i]) == 0:
            res.append('0')
        elif int(num_add1[i]) + int(num_add2[i]) == 1:
            res.append('1')
        elif int(num_add1[i]) + int(num_add2[i]) == 2:
            res.append('0')
            if i > 0:
                num_add1 = num_add1[:i-1]+str(int(num_add1[i-1])+1)+num_add1[i:]
            elif i == 0:
                res.append('1')
            if i <= 1:
                flag_trans += 1
        elif int(num_add1[i]) + int(num_add2[i]) == 3:
            res.append('1')
            if i > 0:
                num_add1 = num_add1[:i-1]+str(int(num_add1[i-1])+1)+num_add1[i:]
            elif i == 0:
                res.append('1')
            if i <= 1:
                flag_trans += 1
    res.reverse()
    if flag_trans == 1:
        digits = len(temp1)
        if digits == 8:
            digits = 16
        elif digits == 16:
            digits = 32
        else:
            return False
        num_add1 = to_reversed(temp1)
        num_add2 = to_reversed(temp2)
        num_add1 = addictional(num_add1)
        num_add2 = addictional(num_add2)
        num_add1 = dir_to_bin(num_add1)
        num_add2 = dir_to_bin(num_add2)
        num_add1 = to_direct(num_add1, digits)
        num_add2 = to_direct(num_add2, digits)
        num_add1 = to_reversed(num_add1)
        num_add2 = to_reversed(num_add2)
        num_add1 = addictional(num_add1)
        num_add2 = addictional(num_add2)
        result = addictonal_sum(num_add1, num_add2)

        return result
    else:
        res = ''.join(res)
        if len(res) > length:
            res = res[1:]
        return res


def action():
    sys1 = sys1Scale.get()          #int
    sys2 = sys2Scale.get()          #int
    sysRes = resScale.get()         #int

    firstInp = num1.get()           #str
    secondInp = num2.get()          #str

    if not check(firstInp, sys1):
        mb.showerror('Ошибка!', 'Неверно введено первое число!')
        return
    elif not check(secondInp, sys2):
        mb.showerror('Ошибка!', 'Неверно введено второе число!')
        return

    if op.get() == 0:  # radio 0 = sum
        digits = 0
        firstNumDec = any_to_decimal(firstInp, sys1)
        secondNumDec = any_to_decimal(secondInp, sys2)
        firstNumBin = decimal_to_any(firstNumDec, 2)
        secondNumBin = decimal_to_any(secondNumDec, 2)

        if firstNumDec < 2 ** 7 - 1 and firstNumDec > -2 ** 7 and secondNumDec < 2 ** 7 - 1 and secondNumDec > -2 ** 7:
            digits = 8
        elif firstNumDec < 2 ** 15 - 1 and firstNumDec > -2 ** 15 and secondNumDec < 2 ** 15 - 1 and secondNumDec > -2 ** 15:
            digits = 16
        elif firstNumDec < 2 ** 31 - 1 and firstNumDec > -2 ** 31 and secondNumDec < 2 ** 31 - 1 and secondNumDec > -2 ** 31:
            digits = 32
        else:
            mb.showerror('Ошибка!', 'Разрядность одного из чисел выше 32')
            return

        firstNumDir = to_direct(firstNumBin, digits)
        secondNumDir = to_direct(secondNumBin, digits)
        firstNumRev = to_reversed(firstNumDir)
        secondNumRev = to_reversed(secondNumDir)
        firstNumAddict = addictional(firstNumRev)
        secondNumAddict = addictional(secondNumRev)

        resultAddict = addictonal_sum(firstNumAddict, secondNumAddict)

        resultDir = addictional(to_reversed(resultAddict))
        resultBin = dir_to_bin(resultDir)
        resultDec = any_to_decimal(resultBin, 2)
        result = decimal_to_any(resultDec, sysRes)

        res.set(result)

    elif op.get() == 1:  # radio 1 = minus
        print('minus')
    elif op.get() == 2:  # radio 2 = mult
        print('mult')
    elif op.get() == 3:  # radio 3 = division
        print('division')


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

op = IntVar()
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
result = Label(textvariable=res, bd=4, bg='#67ACB6', font='arial 15')
result.place(height=65, width=630, y=400, x=150)

resScale = Scale(orient=HORIZONTAL, length=110, from_=2, to=16, tickinterval=14, resolution=1, bg='#67ACB6',
                 font='arial 12 bold', fg='#222222', activebackground='#FFAB00', bd=0, highlightthickness=0)
resScale.place(width=110, y=400, x=15)

btn = Button(text='Вычислить', bg='#DCDCDC', font='Arial 25 bold', activebackground='#DCDCDC', fg='#222222',
             bd=3, command=action)
btn.place(height=100, width=200, y=210,x=300)


root.mainloop()
