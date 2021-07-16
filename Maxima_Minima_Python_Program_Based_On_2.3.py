from sympy.parsing.sympy_parser import parse_expr
import numpy as np
import sympy as sypy
import os
import time

def clrscr():
    if os.name == 'posix': 
        _ = os.system('clear')
    else: 
        _ = os.system('cls')

if name = '__main__':
    while True:
        minima = int(0)
        maxima = int(0)
        x = sypy.Symbol('x')
        y = sypy.Symbol('y')
        z = sypy.Symbol('z')
        r = sypy.Symbol('r')
        t = sypy.Symbol('t')
        s = sypy.Symbol('s')
        L = sypy.Symbol('L')

        print("\nMIN - MAX Of Quadratic Equations \n\n1. Two Variable Equation\n2. Three Variable using Lagrange Multiplier\n3. Quit \n\n\n Made By - \n\tKhush Ramani\tCSE - C\tIU2041230069")
        choice = int(input('\n\nSelect Your Choice: '))

        if choice == 3:
            break

        elif choice == 1:
            User_equation = input('Enter the equation to Find Min and Max for :')
            maineq = parse_expr(User_equation)

            eq1 = sypy.diff(maineq,x)    #Fx=0
            eq2 = sypy.diff(maineq,y)    #Fy=0
            eq3 = sypy.diff(eq1,x)       #Fxx=0
            eq4 = sypy.diff(eq2,y)       #Fyy=0
            eq5 = sypy.diff(eq1,y)       #Fxy=0
            print('\n\nFx = {}\nFy = {}\nFxx = {}\nFyy = {}\nFxy = {}\n'.format(eq1,eq2,eq3,eq4,eq5))

            solution = sypy.solve([eq1,eq2], dict=True)
            print('\nPossible Values Are : ')
            for i in range(len(solution)):
                print('\t{}'.format(solution[i]))

            for i in range(len(solution)):
                r = eq3.subs(solution[i])
                t = eq4.subs(solution[i])
                s = eq5.subs(solution[i])
                eq6 = r*t-s**2
                if eq6 > 0:
                    if r>0 and t>0:     #minima
                        mnmum = maineq.subs(solution[i]).evalf()
                        if np.isreal(mnmum):
                            print('\n\nThe minimum value = {} at {}'.format(mnmum,solution[i]))
                    if r<0 and t<0:     #maxima
                        mxmum = maineq.subs(solution[i]).evalf()
                        if np.isreal(mxmum):
                            print('\n\nThe maximum value = {} at {}'.format(mxmum,solution[i]))
            input("\n\nPress Enter to continue...")
            clrscr()


        elif choice == 2:
            User_equation = input('\n\nEnter the equation to Find Min and Max for :')
            maineq = parse_expr(User_equation)

            User_equation2 = input('\n\nEnter the constant equation :')     
            consteq = parse_expr(User_equation2)

            langfunc = maineq + L*consteq       #L = lang multiplier
            sypy.simplify(langfunc)
            print('\n\nLangrange Function = {}'.format(langfunc))

            eq1 = diff(langfunc,x)
            eq2 = diff(langfunc,y)
            eq3 = diff(langfunc,z)
            print('\n\nFx = {}\nFy = {}\nFz = {}\n'.format(eq1,eq2,eq3))

            solutionL = sypy.solve([eq1, eq2, eq3, consteq], dict = True)
            print('\nPossible Values Are : ')
            for i in range(len(solutionL)):
                print('\t{}\n'.format(solutionL[i]))

            for i in range(len(solutionL)):
                answer = maineq.subs(solutionL[i]).evalf()
                if np.isreal(answer):
                    print('\nThe value of Function at {} = {}'.format(solutionL[i],answer))
            input("\n\nPress Enter to continue...")
            clrscr()


        else:
            print("Invalid choice, please choose again\n")
            input("\nPress Enter to continue...")
            clrscr()
