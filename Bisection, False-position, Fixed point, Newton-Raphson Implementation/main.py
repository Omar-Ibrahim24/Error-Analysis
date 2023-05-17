import tkinter as tk
from sympy import *
import math
expression = ""
xlower = ""
xupper = ""
tolerence = ""
iterations = ""
def function(x,equation):
    y=eval(equation)
    return y

def solvex(e):
    x, y = symbols('x y')
    e = translator(e)
    expn = eval(e)
    return expn

def translator(equation):
    length = len(equation)
    flag = False
    counter = 0
    translated_equation = ""
    i = 0

    # Handle 1/9  and 7^1/3 for example cases
    if equation[0].isdigit() and equation[1] == '^':
        translated_equation = f'x**{equation[4:]}-{equation[0]}'
        flag = True
    elif equation[0].isdigit() and equation[1] == '/' and 0 <= int(equation[2:]) <= 9:
        translated_equation = f'x-{equation}'
        flag = True

    if flag == False:
        while (i != length):
            # Handle Spaces
            if equation[i] == ' ':
                counter = 1
                pass
            # sin and cos First case : sin x -> sin(    Second case : 2sin x -> 2*sin(
            elif (equation[i:i + 3] == 'sin') or (equation[i:i + 3] == 'cos'):
                if i == 0:
                    counter = 3
                    translated_equation += f'math.{equation[i:i + 3]}'
                elif equation[i - 1].isdigit():
                    counter = 3
                    translated_equation += f'*math.{equation[i:i + 3]}'
                else:
                    counter = 3



            # exponential
            elif equation[i] == 'e':
                if i == 0:
                    translated_equation += f'math.e'
                    counter = 1
                elif equation[i - 1].isdigit():
                    translated_equation += f'*math.e'
                    counter = 1
                else:
                    translated_equation += f'math.e'
                    counter = 1


            # Power
            elif equation[i] == '^':
                translated_equation += '**'
                counter = 1

            # First case: sin x then == sin(x)   Second case  sin2x == sin(2*x)
            elif len(translated_equation) > 0 and (equation[i - 4:i] == "sin(" or equation[i - 4:i] == "cos("):
                if translated_equation[-1] == '(' and equation[i] == 'x':
                    translated_equation += f'{equation[i]}'
                    counter = 1
                if translated_equation[-1] == '(' and equation[i] != 'x':
                    translated_equation += f'{equation[i]}*{equation[i + 1]}'
                    counter = 2

            # Polynomial
            elif equation[i] == 'x':
                if i == 0:
                    translated_equation += 'x'
                    counter = 1
                elif equation[i - 1].isdigit():
                    translated_equation += '*x'
                    counter = 1
                else:
                    translated_equation += 'x'
                    counter = 1

            else:
                translated_equation += equation[i]
                counter = 1

            i += counter
    print("translated equation is :", translated_equation)
    return translated_equation

def getxl(xl):
    global xlower
    xlower = xl.get(1.0, "end")

def getxu(xu):
    global xupper
    xupper = xu.get(1.0, "end")

def gettol(tol):
    global tolerence
    tolerence = tol.get(1.0, "end")

def getitr(itr):
    global iterations
    iterations = itr.get(1.0, "end")

def eval_bisection(xl, xu, epislon, iterations, equation):
    iterator = 1
    e_a = 10000.0
    flag = True
    table = tk.Toplevel(project1)
    table.geometry("500x500")
    table.title("result")
    iteration_label1 = tk.Label(table, text="#")
    iteration_label1.grid(row=0, column=0)
    iteration_label2 = tk.Label(table, text="xl")
    iteration_label2.grid(row=0, column=1)
    iteration_label3 = tk.Label(table, text="xu")
    iteration_label3.grid(row=0, column=2)
    iteration_label4 = tk.Label(table, text="xr")
    iteration_label4.grid(row=0, column=3)
    iteration_label5 = tk.Label(table, text="fxr")
    iteration_label5.grid(row=0, column=4)
    iteration_label6 = tk.Label(table, text="error")
    iteration_label6.grid(row=0, column=5)
    total=[]
    while e_a > epislon and iterator < iterations:
        if function(xl, equation) * function(xu, equation) < 0:
            xr = (xl + xu) / 2
            fxr=function(xr,equation)
            print("iteration number :",iterator)
            print("xlower is :",xl)
            print("xupper is :",xu)
            print("xaverage is :",xr)
            print("function of xr is :",function(xr,equation))

            if function(xl, equation) < function(xu, equation):
                if function(xr, equation) < 0:
                    xl = xr
                else:
                    xu = xr
            else:
                if function(xr, equation) < 0:
                    xu = xr
                else:
                    xl = xr

            if iterator == 1:
                #   print("relative approxmate error is ",e_a)
                pass

            else:
                e_a = abs((float(xr - xr_old) / float(xr))) * 100
                # print("relative approxmate error is ",e_a)
            xr_old = xr
            total.append([iterator,xl, xu, xr,fxr, e_a])
            iterator += 1
            # total[0][3] = "-----"
            # iteration_label = tk.Label(table, text=i)
            # iteration_label.grid(row=i, column=j)
        else:
            print("No Root\n")
            print("XLower and X upper Both return same sign Output... Please Enter Another Interval\n")
            flag = False
            break;
    if flag == True:
        total[0][5] = "-----"
        for i in range(iterator-1):
            for j in range(6):
                iteration_label = tk.Label(table, text=total[i][j])
                iteration_label.grid(row=i+1, column=j)
        print(total)
        root = "Root equal: "
        root += str(xr)
        result = tk.Message(table, text=root)
        result.grid(row=i+2)
        leo = solvex(expression)
        print(leo)
        return xr

def FalsePosition(xl, xu, epislon, iterations, equation):
    iterator = 1
    e_a = 10000.0
    flag = True
    table = tk.Toplevel(project1)
    table.geometry("700x400")
    table.title("result")
    iteration_label1 = tk.Label(table, text="#")
    iteration_label1.grid(row=0, column=0)
    iteration_label2 = tk.Label(table, text="xl")
    iteration_label2.grid(row=0, column=1)
    iteration_label3 = tk.Label(table, text="xu")
    iteration_label3.grid(row=0, column=2)
    iteration_label4 = tk.Label(table, text="xr")
    iteration_label4.grid(row=0, column=3)
    iteration_label5 = tk.Label(table, text="fxr")
    iteration_label5.grid(row=0, column=4)
    iteration_label6 = tk.Label(table, text="error")
    iteration_label6.grid(row=0, column=5)
    total = []
    while e_a > epislon and iterator < iterations:
        if function(xl, equation) * function(xu, equation) < 0:
            xr = (xu * function(xl, equation) - xl * function(xu, equation)) / (
                        function(xl, equation) - function(xu, equation))
            fxr = function(xr, equation)
            if (function(xr, equation) == 0):
                return xr

            print("iteration number: ", iterator)
            print("xlower is: ", xl)
            print("xupper is: ", xu)
            print("xaverage is: ", xr)
            print("function of xr is: ", function(xr, equation))

            if function(xl, equation) < function(xu, equation):
                if function(xr, equation) < 0:
                    xl = xr
                else:
                    xu = xr

            else:
                if function(xr, equation) < 0:
                    xu = xr
                else:
                    xl = xr

            if iterator == 1:

                print("relative approxmate error is: ", e_a)
                pass

            else:
                e_a = abs((float(xr - xr_old) / float(xr))) * 100
                print("relative approxmate error is: ", e_a)

            xr_old = xr
            total.append([iterator, xl, xu, xr, fxr, e_a])
            iterator += 1
        else:
            print("No Root: ")
            flag = False
            break
    if flag == True:
        total[0][5] = "-----"
        for i in range(iterator - 1):
            for j in range(6):
                iteration_label = tk.Label(table, text=total[i][j])
                iteration_label.grid(row=i + 1, column=j)
        print(total)
        root = "Root equal: "
        root += str(xr)
        result = tk.Message(table, text=root)
        result.grid(row=i + 2)
        return xr

def FixedPoint(x0, epislon, iterations, equation):
    x, y = symbols('x y')
    iterator = 1
    e_a = 10000.0
    flag = True
    differn = Derivative(equation, x)
    differ_evaluate = str(differn.doit())
    table = tk.Toplevel(project1)
    table.geometry("700x400")
    table.title("result")
    iteration_label1 = tk.Label(table, text="#")
    iteration_label1.grid(row=0, column=0)
    iteration_label2 = tk.Label(table, text="Xold")
    iteration_label2.grid(row=0, column=1)
    iteration_label3 = tk.Label(table, text="xnew")
    iteration_label3.grid(row=0, column=2)
    iteration_label6 = tk.Label(table, text="error")
    iteration_label6.grid(row=0, column=3)
    total = []
    while e_a > epislon and iterator < iterations:
        if abs(function(x0, differ_evaluate)) < 1:
            print("equation is:", equation)
            print("differnation is ", differ_evaluate)
            print("iteration number: ", iterator)
            print("xold is: ", x0)
            xnew = function(x0, equation)
            print("x new  is: ", xnew)

            e_a = abs((xnew - x0) / xnew) * 100
            print("error is: ", e_a)

            if (e_a == 0):
                return xnew

            x0 = xnew
            total.append([iterator, x0, xnew, e_a])
            iterator += 1
        else:
            print("Function will diverge")
            flag = False
            break;
    if flag == True:
        for i in range(iterator - 1):
            for j in range(4):
                iteration_label = tk.Label(table, text=total[i][j])
                iteration_label.grid(row=i + 1, column=j)
        print(total)
        root = "Root equal: "
        root += str(xnew)
        result = tk.Message(table, text=root)
        result.grid(row=i + 2)
        return xnew

def eval_newton(x0,epislon,iterations,equation):
    x, y = symbols('x y')
    iterator=1
    e_a=10000.0
    differn = Derivative(equation, x)
    differ_evaluate=str(differn.doit())
    table = tk.Toplevel(project1)
    table.geometry("700x400")
    table.title("result")
    iteration_label1 = tk.Label(table, text="#")
    iteration_label1.grid(row=0, column=0)
    iteration_label2 = tk.Label(table, text="Xold")
    iteration_label2.grid(row=0, column=1)
    iteration_label3 = tk.Label(table, text="xnew")
    iteration_label3.grid(row=0, column=2)
    iteration_label6 = tk.Label(table, text="error")
    iteration_label6.grid(row=0, column=3)
    total = []
    while e_a>epislon and  iterator<iterations:
      print("iteration number: ",iterator)
      print("xold is: ",x0)
      xnew=x0-function(x0,equation)/function(x0,differ_evaluate)
      print("x new  is: ",xnew)
      e_a=abs((xnew-x0)/xnew)*100
      print("error is: ",e_a)

      if(e_a==0):
        return xnew

      x0=xnew
      total.append([iterator, x0, xnew, e_a])
      iterator+=1
    for i in range(iterator - 1):
        for j in range(4):
            iteration_label = tk.Label(table, text=total[i][j])
            iteration_label.grid(row=i + 1, column=j)


    print(total)
    root = "Root equal: "
    root += str(xnew)
    result = tk.Message(table, text=root)
    result.grid(row=i + 2)
    return xnew

def eval_secant(x0,x1,epislon,iterations,equation):
    iterator=1
    e_a=10000.0
    table = tk.Toplevel(project1)
    table.geometry("700x400")
    table.title("result")
    iteration_label1 = tk.Label(table, text="#")
    iteration_label1.grid(row=0, column=0)
    iteration_label2 = tk.Label(table, text="X(i-1)")
    iteration_label2.grid(row=0, column=1)
    iteration_label3 = tk.Label(table, text="F(X(i-1))")
    iteration_label3.grid(row=0, column=2)
    iteration_label4 = tk.Label(table, text="X(i)")
    iteration_label4.grid(row=0, column=3)
    iteration_label5 = tk.Label(table, text="F(X(i))")
    iteration_label5.grid(row=0, column=4)
    iteration_label6 = tk.Label(table, text="X(i+1)")
    iteration_label6.grid(row=0, column=5)
    iteration_label7 = tk.Label(table, text="error")
    iteration_label7.grid(row=0, column=6)
    total = []
    while e_a>epislon and  iterator<iterations:
      print("iteration number: ",iterator)
      print("xi-1 is: ",x0)
      print("xi is: ",x1)
      print("function of xi-1 is: ",function(x0,equation))
      print("function of xi is: ",function(x1,equation))

      # xnew=(x0*function(x1,equation)-x1*function(x0,equation))/function(x1,equation)-function(x0,equation)
      xnew=x1-(function(x1,equation)*(x1-x0)/(function(x1,equation)-function(x0,equation)))
      print("x new  is: ",xnew)
      e_a=abs((xnew-x1)/xnew)*100
      print("error is: ",e_a)

      if(e_a==0):
        return xnew
      total.append([iterator, x0, function(x0, equation), x1, function(x1, equation), xnew, e_a])
      x0=x1
      x1=xnew
      iterator+=1
    for i in range(iterator - 1):
        for j in range(7):
            iteration_label = tk.Label(table, text=total[i][j])
            iteration_label.grid(row=i + 1, column=j)


    print(total)
    root = "Root equal: "
    root += str(xnew)
    result = tk.Message(table, text=root)
    result.grid(row=i + 2)
    return xnew

def eval_mod_secant(x0,percentage,epislon,iterations,equation):
    p=percentage/100
    iterator=1
    e_a=10000.0
    table = tk.Toplevel(project1)
    table.geometry("700x400")
    table.title("result")
    iteration_label1 = tk.Label(table, text="#")
    iteration_label1.grid(row=0, column=0)
    iteration_label2 = tk.Label(table, text="X(i)")
    iteration_label2.grid(row=0, column=1)
    iteration_label3 = tk.Label(table, text="F(X(i))")
    iteration_label3.grid(row=0, column=2)
    iteration_label4 = tk.Label(table, text="P*X(i)")
    iteration_label4.grid(row=0, column=3)
    iteration_label5 = tk.Label(table, text="F(P*X(i))")
    iteration_label5.grid(row=0, column=4)
    iteration_label6 = tk.Label(table, text="X(i+1)")
    iteration_label6.grid(row=0, column=5)
    iteration_label7 = tk.Label(table, text="error")
    iteration_label7.grid(row=0, column=6)
    total = []
    while e_a>epislon and  iterator<iterations:
      print("iteration number: ",iterator)
      print("xi is: ",x0)
      print("function of xi is: ",function(x0,equation))

      xnew=x0-(function(x0,equation)*(p*x0)/(function(x0+p*x0,equation)-function(x0,equation)))
      print("x new  is: ",xnew)
      e_a=abs((xnew-x0)/xnew)*100
      print("error is: ",e_a)

      if(e_a==0):
        return xnew
      total.append([iterator, x0, function(x0, equation), x0+p*x0, function(x0+p*x0,equation), xnew, e_a])
      x0=xnew
      iterator+=1
    for i in range(iterator - 1):
        for j in range(7):
            iteration_label = tk.Label(table, text=total[i][j])
            iteration_label.grid(row=i + 1, column=j)


    print(total)
    root = "Root equal: "
    root += str(xnew)
    result = tk.Message(table, text=root)
    result.grid(row=i + 2)
    return xnew

def append_equation(x):
    global expression
    expression += str(x)
    equation.delete(1.0, "end")
    equation.insert(1.0, expression)

def clear():
    global expression
    expression = ""
    equation.delete(1.0, "end")

def bisection():
    bisectionW = tk.Toplevel(project1)
    bisectionW.geometry("300x150")
    bisectionW.title("Bisection")
    xl_label = tk.Label(bisectionW, text="Enter Lower Bound:")
    xl_label.grid(row=0, column=0)
    xl = tk.Text(bisectionW, height=1, width=21)
    xl.grid(row=0, column=1)
    xu_label = tk.Label(bisectionW, text="Enter Upper Bound:")
    xu_label.grid(row=1, column=0)
    xu = tk.Text(bisectionW, height=1, width=21)
    xu.grid(row=1, column=1)
    iter_label = tk.Label(bisectionW, text="Enter no of iterations:" )
    iter_label.grid(row=2, column=0)
    iter = tk.Text(bisectionW, height=1, width=21)
    iter.grid(row=2, column=1)
    tol_label = tk.Label(bisectionW, text="Enter the tolerance:")
    tol_label.grid(row=3, column=0)
    tol = tk.Text(bisectionW, height=1, width=21)
    tol.grid(row=3, column=1)
    evaluate = tk.Button(bisectionW, text="Evaluate", cursor="pirate", command=lambda: eval_bisection(float(xlower), float(xupper), float(tolerence), float(iterations), translator(expression)))
    evaluate.grid(row=4, column=0)
    enter = tk.Button(bisectionW, text="Enter", cursor="pirate", command=lambda:( getxu(xu), getxl(xl), gettol(tol), getitr(iter)))
    enter.grid(row=4, column=1)

def falsi_pos():
    falsi_pos = tk.Toplevel(project1)
    falsi_pos.geometry("300x150")
    falsi_pos.title("Falsi position")
    xl_label = tk.Label(falsi_pos, text="Enter Lower Bound:")
    xl_label.grid(row=0, column=0)
    xl = tk.Text(falsi_pos, height=1, width=21)
    xl.grid(row=0, column=1)
    xu_label = tk.Label(falsi_pos, text="Enter Upper Bound:")
    xu_label.grid(row=1, column=0)
    xu = tk.Text(falsi_pos, height=1, width=21)
    xu.grid(row=1, column=1)
    iter_label = tk.Label(falsi_pos, text="Enter no of iterations:")
    iter_label.grid(row=2, column=0)
    iter = tk.Text(falsi_pos, height=1, width=21)
    iter.grid(row=2, column=1)
    tol_label = tk.Label(falsi_pos, text="Enter the tolerance:")
    tol_label.grid(row=3, column=0)
    tol = tk.Text(falsi_pos, height=1, width=21)
    tol.grid(row=3, column=1)
    evaluate = tk.Button(falsi_pos, text="Evaluate", cursor="pirate", command=lambda: FalsePosition(float(xlower), float(xupper), float(tolerence), float(iterations), translator(expression)))
    evaluate.grid(row=4, column=0)
    enter = tk.Button(falsi_pos, text="Enter", cursor="pirate", command=lambda:(getxu(xu), getxl(xl), gettol(tol), getitr(iter)))
    enter.grid(row=4, column=1)
def fixed_point():
    fixed = tk.Toplevel(project1)
    fixed.geometry("300x150")
    fixed.title("Fixed Point")
    xl_label = tk.Label(fixed, text="Enter Xo:")
    xl_label.grid(row=0, column=0)
    xl = tk.Text(fixed, height=1, width=21)
    xl.grid(row=0, column=1)
    iter_label = tk.Label(fixed, text="Enter no of iterations:")
    iter_label.grid(row=1, column=0)
    iter = tk.Text(fixed, height=1, width=21)
    iter.grid(row=1, column=1)
    tol_label = tk.Label(fixed, text="Enter the tolerance:")
    tol_label.grid(row=2, column=0)
    tol = tk.Text(fixed, height=1, width=21)
    tol.grid(row=2, column=1)
    evaluate = tk.Button(fixed, text="Evaluate", cursor="pirate", command=lambda: FixedPoint(float(xlower), float(tolerence), float(iterations), translator(expression)))
    evaluate.grid(row=4, column=0)
    enter = tk.Button(fixed, text="Enter", cursor="pirate", command=lambda:(getxl(xl), gettol(tol), getitr(iter)))
    enter.grid(row=4, column=1)
def newton():
    newton = tk.Toplevel(project1)
    newton.geometry("300x150")
    newton.title("Newton Point")
    xl_label = tk.Label(newton, text="Enter Xo:")
    xl_label.grid(row=0, column=0)
    xl = tk.Text(newton, height=1, width=21)
    xl.grid(row=0, column=1)
    iter_label = tk.Label(newton, text="Enter no of iterations:")
    iter_label.grid(row=1, column=0)
    iter = tk.Text(newton, height=1, width=21)
    iter.grid(row=1, column=1)
    tol_label = tk.Label(newton, text="Enter the tolerance:")
    tol_label.grid(row=2, column=0)
    tol = tk.Text(newton, height=1, width=21)
    tol.grid(row=2, column=1)
    evaluate = tk.Button(newton, text="Evaluate", cursor="pirate", command=lambda: eval_newton(float(xlower), float(tolerence), float(iterations), translator(expression)))
    evaluate.grid(row=4, column=0)
    enter = tk.Button(newton, text="Enter", cursor="pirate", command=lambda:(getxl(xl), gettol(tol), getitr(iter)))
    enter.grid(row=4, column=1)
def secant():
    secentw = tk.Toplevel(project1)
    secentw.geometry("300x150")
    secentw.title("Secant")
    xl_label = tk.Label(secentw, text="Enter Lower Bound:")
    xl_label.grid(row=0, column=0)
    xl = tk.Text(secentw, height=1, width=21)
    xl.grid(row=0, column=1)
    xu_label = tk.Label(secentw, text="Enter Upper Bound:")
    xu_label.grid(row=1, column=0)
    xu = tk.Text(secentw, height=1, width=21)
    xu.grid(row=1, column=1)
    iter_label = tk.Label(secentw, text="Enter no of iterations:")
    iter_label.grid(row=2, column=0)
    iter = tk.Text(secentw, height=1, width=21)
    iter.grid(row=2, column=1)
    tol_label = tk.Label(secentw, text="Enter the tolerance:")
    tol_label.grid(row=3, column=0)
    tol = tk.Text(secentw, height=1, width=21)
    tol.grid(row=3, column=1)
    evaluate = tk.Button(secentw, text="Evaluate", cursor="pirate", command=lambda: eval_secant(float(xlower), float(xupper), float(tolerence), float(iterations), translator(expression)))
    evaluate.grid(row=4, column=0)
    enter = tk.Button(secentw, text="Enter", cursor="pirate", command=lambda:(getxl(xl), getxu(xu), gettol(tol), getitr(iter)))
    enter.grid(row=4, column=1)
def modsecant():
    msecentw = tk.Toplevel(project1)
    msecentw.geometry("300x150")
    msecentw.title("Secant")
    xl_label = tk.Label(msecentw, text="Enter Xo:")
    xl_label.grid(row=0, column=0)
    xl = tk.Text(msecentw, height=1, width=21)
    xl.grid(row=0, column=1)
    xu_label = tk.Label(msecentw, text="Enter percentage:")
    xu_label.grid(row=1, column=0)
    xu = tk.Text(msecentw, height=1, width=21)
    xu.grid(row=1, column=1)
    iter_label = tk.Label(msecentw, text="Enter no of iterations:")
    iter_label.grid(row=2, column=0)
    iter = tk.Text(msecentw, height=1, width=21)
    iter.grid(row=2, column=1)
    tol_label = tk.Label(msecentw, text="Enter the tolerance:")
    tol_label.grid(row=3, column=0)
    tol = tk.Text(msecentw, height=1, width=21)
    tol.grid(row=3, column=1)
    evaluate = tk.Button(msecentw, text="Evaluate", cursor="pirate", command=lambda: eval_mod_secant(float(xlower), float(xupper), float(tolerence), float(iterations), translator(expression)))
    evaluate.grid(row=4, column=0)
    enter = tk.Button(msecentw, text="Enter", cursor="pirate", command=lambda: (getxl(xl), getxu(xu), gettol(tol), getitr(iter)))
    enter.grid(row=4, column=1)
project1 = tk.Tk(className="Project")
project1.geometry("400x600")
label1 = tk.Label(project1, text="Enter equation:", font=21)
label1.grid(row=0, columnspan=5)
equation = tk.Text(project1, height=2, width=36, font=21)
equation.grid(row=1, column=0, columnspan=5)
btn_1 = tk.Button(project1, text="1", command=lambda: append_equation(1), height=4,  width=13, activebackground="white")
btn_1.grid(row=2, column=0)
btn_2 = tk.Button(project1, text="2", command=lambda: append_equation(2), height=4,  width=13, activebackground="white")
btn_2.grid(row=2, column=1)
btn_3 = tk.Button(project1, text="3", command=lambda: append_equation(3), height=4,  width=13, activebackground="white")
btn_3.grid(row=2, column=2)
btn_plus = tk.Button(project1, text="+", command=lambda: append_equation("+"), height=4,  width=13, activebackground="white")
btn_plus.grid(row=2, column=4)
btn_4 = tk.Button(project1, text="4", command=lambda: append_equation(4), height=4,  width=13, activebackground="white")
btn_4.grid(row=3, column=0)
btn_5 = tk.Button(project1, text="5", command=lambda: append_equation(5), height=4,  width=13, activebackground="white")
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(project1, text="6", command=lambda: append_equation(6), height=4,  width=13, activebackground="white")
btn_6.grid(row=3, column=2)
btn_min = tk.Button(project1, text="-", command=lambda: append_equation("-"), height=4,  width=13, activebackground="white")
btn_min.grid(row=3, column=4)
btn_7 = tk.Button(project1, text="7", command=lambda: append_equation(7), height=4,  width=13, activebackground="white")
btn_7.grid(row=4, column=0)
btn_8 = tk.Button(project1, text="8", command=lambda: append_equation(8), height=4,  width=13, activebackground="white")
btn_8.grid(row=4, column=1)
btn_9 = tk.Button(project1, text="9", command=lambda: append_equation(9), height=4,  width=13, activebackground="white")
btn_9.grid(row=4, column=2)
btn_mult = tk.Button(project1, text="*", command=lambda: append_equation("*"), height=4,  width=13, activebackground="white")
btn_mult.grid(row=4, column=4)
btn_left = tk.Button(project1, text="(", command=lambda: append_equation("("), height=4,  width=13, activebackground="white")
btn_left.grid(row=5, column=0)
btn_0 = tk.Button(project1, text="0", command=lambda: append_equation(0), height=4,  width=13, activebackground="white")
btn_0.grid(row=5, column=1)
btn_right = tk.Button(project1, text=")", command=lambda: append_equation(")"), height=4,  width=13, activebackground="white")
btn_right.grid(row=5, column=2)
btn_div = tk.Button(project1, text="/", command=lambda: append_equation("/"), height=4,  width=13, activebackground="white")
btn_div.grid(row=5, column=4)
btn_cos = tk.Button(project1, text="cos", command=lambda: append_equation("cos("), height=4,  width=13, activebackground="white")
btn_cos.grid(row=6, column=0)
btn_sin = tk.Button(project1, text="sin", command=lambda: append_equation("sin("), height=4,  width=13, activebackground="white")
btn_sin.grid(row=6, column=1)
btn_x = tk.Button(project1, text="x", command=lambda: append_equation("x"), height=4,  width=13, activebackground="white")
btn_x.grid(row=6, column=2)
btn_pow = tk.Button(project1, text="^", command=lambda: append_equation("^"), height=4,  width=13, activebackground="white")
btn_pow.grid(row=6, column=4)
btn_exp = tk.Button(project1, text="e", command=lambda: append_equation("e"), height=4,  width=13, activebackground="white")
btn_exp.grid(row=7, column=0)
btn_dec = tk.Button(project1, text=".",  command=lambda: append_equation("."), height=4,  width=13, activebackground="white")
btn_dec.grid(row=7, column=1)
btn_clr = tk.Button(project1, text="C",  command=clear, height=4,  width=13, activebackground="white")
btn_clr.grid(row=7, column=2)
method = tk.Menubutton(project1, text="Choose method", activebackground="red", font=("Arial", 14), cursor="heart")
method.menu = tk.Menu(method)
method["menu"] = method.menu
method.menu.add_command(label="Bisection", command=bisection)
method.menu.add_command(label="Falsi-position", command=falsi_pos)
method.menu.add_command(label="Fixed point",command=fixed_point)
method.menu.add_command(label="Newton-Raphson",command=newton)
method.menu.add_command(label="Secant", command=secant)
method.menu.add_command(label="Modified secant", command=modsecant)
method.grid(row=9, columnspan=5)
project1.mainloop()