# generates a table of predicted points with Euler's Method

import math

dydx = input("What's the equation of dy/dx?")
n = int(input("How many steps?"))
h = float(input("What's the step length"))
x = float(input("Starting x value"))
y = float(input("Starting y value?"))

# store/display starting value
print("(" + str(x) + "," + str(y) + ")")

# repeat the process of finding x and y values n times
i = 1
while i <= n:

    # find y1
    # y1 = y0 + h*(dy/dx)
    y = y + h*(eval(dydx))

    # find x1
    # x1 = x0 + h
    x = x + h

    # store/display table values
    print("(" + str(round(x,3)) + "," + str(round(y,3)) + ")")


    i = i+1
    