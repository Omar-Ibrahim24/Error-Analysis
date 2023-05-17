from tkinter import *
import re
import numpy as np
import sys

equation = []
guesses = []
numberOfEquation = ""

def gaussian_elimination(matrices):
    names = ['x', 'y', 'z', 'w', 'm', 'n', 'k', 'a', 'b', 'c', 'd']
    table = Toplevel(project2)
    table.geometry("500x500")
    table.title("result")
    n = len(matrices)
    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    output = np.zeros(n)

    # Applying Gauss Elimination
    for i in range(n):
        if matrices[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = matrices[j][i] / matrices[i][i]

            for k in range(n + 1):
                matrices[j][k] = matrices[j][k] - ratio * matrices[i][k]
    print("forward sub is ", matrices)

    # Back Substitution
    output[n - 1] = matrices[n - 1][n] / matrices[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        output[i] = matrices[i][n]

        for j in range(i + 1, n):
            output[i] = output[i] - matrices[i][j] * output[j]

        output[i] = output[i] / matrices[i][i]
    for i in range(int(numberOfEquation)):
        iteration_label1 = Label(table, text=(names[i]))
        iteration_label1.grid(row=0, column=i)
        iteration_label1 = Label(table, text=(output[i]))
        iteration_label1.grid(row=1, column=i)



def Gaussian_Siedel(matrices, iterations, epislon, old):
    names = ['x', 'y', 'z', 'w', 'm', 'n', 'k', 'a', 'b', 'c', 'd']
    table = Toplevel(project2)
    table.geometry("500x500")
    table.title("result")
    a = []  # A
    b = []  # B
    n = len(matrices)
    error = [10000000] * n  # Calculate error for x,y,z,.....
    # old=[1,0,1];                # Calcualte old values for x,y,z,.....
    new = [0] * n  # Calcualte new values for x,y,z,.....
    solution = []  # Solution

    # Split matrix to get A and B
    for i in range(0, n):
        a.append(matrices[i][0:len(matrices[i]) - 1])
        b.append(matrices[i][-1])

    i = 1  # Counter For iterations
    while (i != iterations):
        # print("iteration number:", i)
        flag = False

        if n >= 3:
            solution.append(list(old))

            new[0] = (b[0] - (a[0][1] * old[1]) - (a[0][2] * old[2])) / a[0][0]
            new[1] = (b[1] - (a[1][0] * new[0]) - (a[1][2] * old[2])) / a[1][1]
            new[2] = (b[2] - (a[2][0] * new[0]) - (a[2][1] * new[1])) / a[2][2]

            for m in range(0, n):
                error[m] = abs((new[m] - old[m]) / new[m]) * 100

            old[0] = new[0]
            old[1] = new[1]
            old[2] = new[2]

        if n >= 4:
            solution.append(list(old))
            new[0] = (b[0] - (a[0][1] * old[1]) - (a[0][2] * old[2]) - (a[0][3] * old[3])) / a[0][0]
            new[1] = (b[1] - (a[1][0] * new[0]) - (a[1][2] * old[2]) - (a[1][3] * old[3])) / a[1][1]
            new[2] = (b[2] - (a[2][0] * new[0]) - (a[2][1] * new[1]) - (a[2][3] * old[3])) / a[2][2]
            new[3] = (b[3] - (a[3][0] * new[0]) - (a[3][1] * new[1]) - (a[3][2] * new[2])) / a[3][3]
            for m in range(0, n):
                error[m] = abs((new[m] - old[m]) / new[m]) * 100
            old[0] = new[0]
            old[1] = new[1]
            old[2] = new[2]
            old[3] = new[3]

        for k in range(0, n):
            if (error[k] > epislon):  ### Check if one of the errors is larger than epislon so we will iterate again
                flag = True
                break

        if flag == False:  #### This means that eror for x,y,z is lower than epislon
            break

        i = i + 1  # iteration +1

    for i in range(int(numberOfEquation)):
        iteration_label1 = Label(table, text=(names[i]))
        iteration_label1.grid(row=0, column=i+1)
    iteration_label1.grid(row=0, column= i  + 2)

    for j in range(iterations):
        for i in range(int(numberOfEquation) ):
            iteration_label1 = Label(table, text=solution[j][i])
            iteration_label1.grid(row=j+1, column=i+1)
# 10x+2y-z=27
# -3x-6y+2z=-61.5
# x+y+5z=-21.5

def getno(nOfEqns):
    global numberOfEquation
    numberOfEquation = nOfEqns.get(1.0, "end")

def readequation(equation):
    counter = 0
    matrices = []
    for j in range(0, len(equation)):
        if '=' not in equation[j]:
            equation[j] = equation[j][0:len(equation[j]) - 2] + "=" + str(-int(equation[j][-2:]))  ##"3x+2y+z-6","2x+3y-7","2z-4"    if example doesnot contain '=' so take all string except last 2 characters
            ## and append '=' after that put the integer with opposite its sign

    print(equation)

    for i in equation:
        z = re.findall(r'[\d\.\-\+]+', i)  # Split each equation to get coffeicients

        for j in range(0, len(z)):
            if z[j] == '-':  # Check if '-' put -1
                z[j] = '-1'
            elif z[j] == '+':  # Check if '+' put 1
                z[j] = '1'

        if i[0] == 'x':  # if x+2y+3z   consider coffiecent of x as 1
            z.insert(0, '1')
        if 'x' not in i:
            z.insert(0, '0')

        if i[0] == 'y':  # y+3z=45    consider coffiecent of y as 1
            z.insert(1, '1')
        if i[0] == 'z':  # z=45    consider coffiecent of z as 1
            z.insert(2, '1')
        if i[0] == 'w':
            z.insert(3, '1')
        if i[0] == 'm':
            z.insert(4, '1')
        if i[0] == 'n':
            z.insert(5, '1')
        if i[0] == 'k':
            z.insert(6, '1')
        if i[0] == 'a':
            z.insert(7, '1')
        if i[0] == 'b':
            z.insert(8, '1')
        if i[0] == 'c':
            z.insert(9, '1')
        if i[0] == 'd':
            z.insert(10, '1')

        if 'y' not in i and len(equation) >= 2:  # if x or y or z are missing consider this value in matrix as 0
            z.insert(1, '0')
        if 'z' not in i and len(equation) >= 3:
            z.insert(2, '0')
        if 'w' not in i and len(equation) >= 4:
            z.insert(3, '0')
        if 'm' not in i and len(equation) >= 5:
            z.insert(4, '0')
        if 'n' not in i and len(equation) >= 6:
            z.insert(5, '0')
        if 'k' not in i and len(equation) >= 7:
            z.insert(6, '0')
        if 'a' not in i and len(equation) >= 8:
            z.insert(7, '0')
        if 'b' not in i and len(equation) >= 9:
            z.insert(8, '0')
        if 'c' not in i and len(equation) >= 10:
            z.insert(9, '0')
        if 'd' not in i and len(equation) >= 11:
            z.insert(10, '0')

        matrices.append(z)
    matrices = [list(map(float, m)) for m in matrices]
    return matrices



def gaussianW():
    # print(str(equation) + "lolo")
    takeEq = Toplevel(project2)
    takeEq.geometry("400x200")
    takeEq.title("Equations")
    equ = []

    for j in range(int(numberOfEquation)):
            l = Label(takeEq, text='equation' + str(j + 1))
            l.pack()
            e = Entry(takeEq)
            e.pack()
            equ.append(e)


    def output():
        for i in equ:
            equation.append(i.get())
    submit = Button(takeEq,text="submit", command=lambda: output(), activebackground="white")
    submit.pack()
    btn_no = Button(takeEq, text="Eval", command=lambda: gaussian_elimination(readequation(equation)), activebackground="white")
    btn_no.pack()

def siedelW():
    takeEq = Toplevel(project2)
    takeEq.geometry("400x200")
    takeEq.title("Equations")
    equ = []
    guess = []

    for j in range(int(numberOfEquation)):
            l = Label(takeEq, text='equation' + str(j + 1))
            l.pack()
            e = Entry(takeEq)
            e.pack()
            equ.append(e)
            l2 = Label(takeEq, text='guess' + str(j + 1))
            l2.pack()
            e2 = Entry(takeEq)
            e2.pack()
            guess.append(e2)
    iterations_text = Label(takeEq, text="Enter no of iteration")
    iterations_text.pack()
    iterations = Entry(takeEq)
    iterations.pack()
    epsilon_text = Label(takeEq, text="Enter epsilon")
    epsilon_text.pack()
    epsilon = Entry(takeEq)
    epsilon.pack()

    def output():
        for i in equ:
            equation.append(i.get())
        for i in guess:
            guesses.append(float(i.get()))
    submit = Button(takeEq,text="submit", command=lambda: output(), activebackground="white")
    submit.pack()
    btn_no = Button(takeEq, text="Eval", command=lambda: Gaussian_Siedel(readequation(equation), int(iterations.get()), float(epsilon.get()), guesses), activebackground="white")
    btn_no.pack()

project2 = Tk()
project2.title("project2")
project2.geometry("200x200")
label = Label(project2, text="Enter number of equations:")
label.grid(row=0)

nOfEqns = Text(project2, height=1, width=24)
nOfEqns.grid(row=1)
btn_no = Button(project2, text="Enter",  command=lambda:getno(nOfEqns), activebackground="white")
btn_no.grid(row=2)
btn_m1 = Button(project2, text="Gaussian elimination",  command=lambda: gaussianW(), activebackground="white")
btn_m1.grid(row=3)
btn_m2 = Button(project2, text="Gaussian siedel",  command=lambda: siedelW(), activebackground="white")
btn_m2.grid(row=4)

mainloop()