from sympy import limit, Symbol
import matplotlib.pyplot as plt
import numpy as np

def graph(function, pointInX=0):
    #DEFINING X AXIS RANGE
    x = np.arange(-11, 11, 1)
    #EVALUATING THE FUNCTION
    y = eval(function)
    pointInY = evalInPoint(str(pointInX), function)
    #DEFINING THE GRAPH'S TITLE
    plt.title(f'{function_type}: {function}')
    #DEFINING Y AXIS RANGE
    plt.ylim([-100, 100])
    #SHOW AXES
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    #SHOW LINES IN THE GRAPH
    plt.grid()
    plt.plot(np.where(x == pointInX-11), [pointInY], marker='.', markersize=10, markeredgecolor="red", markerfacecolor="red")
    plt.plot(x, y)
    plt.show()

def evalInPoint(pointInX, function):
    if func_type == 'Irrational' and point < 0:
        pointY = 'Imaginary number'
    else:
        pointY = eval(function.replace('x', point))
    print(point, pointY)

def getFunctionType(function):
    if ') / (' in function:
        function_type = 'Rational'
        return function_type
    elif '**(0' in function or '**0' in function:
        function_type = 'Irrational'
        return function_type
    else:
        function_type = 'Polinomical'
        return function_type


def getFunctionLimits(function, point):
    x = Symbol('x')
    limits = limit(function, x, point), limit(function, x, point, '-')
    return f'limit of {function} when x = {point} \n {limits}'





def main():
    function = str(input("Enter the function: "))
    point = int(input("Enter the point: "))
    func_type = getFunctionType(function)
    fdex = evalInPoint(str(point), function)
    limits = getFunctionLimits(function, point)
    graph(function, point)

    print(f'The function type is: {func_type}')
    print(f'The function in that point is equal to: {fdex}')
    print(f'Limits of the funciton: {limits}')

main()

#function = str(input("Enter the function: "))
#pointX = int(input("Enter the point: "))
#
#if ') / (' in function:
#    function_type = 'Rational'
#elif '**(0' in function or '**0' in function:
#    function_type = 'Irrational'
#else:
#    function_type = 'Polinomical'
#
#if function_type == 'Irrational' and pointX < 0:
#    pointY = 'Imaginary number'
#else:
#    pointY = eval(function.replace('x', str( pointX )))
#
#x = Symbol('x')
#limits = limit(function, x, pointX), limit(function, x, pointX, '-')
#limits = f'limit of {function} when x = {pointX} \n {limits}'
#
#numpyX = np.arange(-11, 11, 1)
#fx = eval(function)
#print(fx)
#plt.title(f'{function_type}: {function}')
#plt.ylim([-100, 100])
#plt.axhline(0, color='black')
#plt.axvline(0, color='black')
#plt.grid()
#plt.plot(np.where(x == pointX-11), [pointY], marker='.', markersize=10, markeredgecolor="red", markerfacecolor="red")
#plt.plot(x, fx)
#plt.show()
