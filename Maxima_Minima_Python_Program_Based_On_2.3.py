from numpy import sin, pi, isreal, exp
from sympy import solve, Symbol, diff, simplify, evalf
from sympy.parsing.sympy_parser import parse_expr
from os import system, name
from time import sleep 

def clrscr():
    if name == 'posix': 
        _ = system('clear')
    else: 
        _ = system('cls')


while True:
    minima = int(0)
    maxima = int(0)
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    r = Symbol('r')
    t = Symbol('t')
    s = Symbol('s')
    L = Symbol('L')

    print("\nMIN - MAX Of Quadratic Equations \n\n1. Two Variable Equation\n2. Three Variable using Lagrange Multiplier\n3. Quit \n\n\n Made By - \n\tKhush Ramani\tCSE - C\tIU2041230069")
    choice = input('\n\nSelect Your Choice: ')

    if choice == '3':
        break


    elif choice == '1':
        User_equation = input('Enter the equation to Find Min and Max for :')
        maineq = parse_expr(User_equation)

        eq1 = diff(maineq,x)    #Fx=0
        eq2 = diff(maineq,y)    #Fy=0
        eq3 = diff(eq1,x)       #Fxx=0
        eq4 = diff(eq2,y)       #Fyy=0
        eq5 = diff(eq1,y)       #Fxy=0
        print('\n\nFx = {}\nFy = {}\nFxx = {}\nFyy = {}\nFxy = {}\n'.format(eq1,eq2,eq3,eq4,eq5))

        solution = solve([eq1,eq2], dict=True)
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
                    if isreal(mnmum):
                        print('\n\nThe minimum value = {} at {}'.format(mnmum,solution[i]))
                if r<0 and t<0:     #maxima
                    mxmum = maineq.subs(solution[i]).evalf()
                    if isreal(mxmum):
                        print('\n\nThe maximum value = {} at {}'.format(mxmum,solution[i]))
        input("\n\nPress Enter to continue...")
        clrscr()


    elif choice == '2':
        User_equation = input('\n\nEnter the equation to Find Min and Max for :')
        maineq = parse_expr(User_equation)

        User_equation2 = input('\n\nEnter the constant equation :')     
        consteq = parse_expr(User_equation2)

        langfunc = maineq + L*consteq       #L = lang multiplier
        simplify(langfunc)
        print('\n\nLangrange Function = {}'.format(langfunc))

        eq1 = diff(langfunc,x)
        eq2 = diff(langfunc,y)
        eq3 = diff(langfunc,z)
        print('\n\nFx = {}\nFy = {}\nFz = {}\n'.format(eq1,eq2,eq3))

        solutionL = solve([eq1, eq2, eq3, consteq], dict = True)
        print('\nPossible Values Are : ')
        for i in range(len(solutionL)):
            print('\t{}\n'.format(solutionL[i]))

        for i in range(len(solutionL)):
            answer = maineq.subs(solutionL[i]).evalf()
            if isreal(answer):
                print('\nThe value of Function at {} = {}'.format(solutionL[i],answer))
        input("\n\nPress Enter to continue...")
        clrscr()


    else:
        print("Invalid choice, please choose again\n")
        input("\nPress Enter to continue...")
        clrscr()