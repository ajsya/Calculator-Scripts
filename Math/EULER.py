# generates a table of predicted points with Euler's Method

# imports all the functions in math in case user calls upon them in their dy/dx input
from math import *

print("You must enter dy/dx in terms of how python does math or else you will get an error. \n Ex. 3x^2 + 9(y-1) becomes 3*x**2 + 9*(y-1) \n Basic transcendental functions should work as inputed by the calculator (use buttons). \n x and y must be lowercase.")
dydx = input("What's the equation of dy/dx?")
n = int(input("How many steps?"))
h = float(input("What's the step length"))
x = float(input("Starting x value"))
y = float(input("Starting y value?"))

# store/display starting value
print("Estimated points on equation of line")
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

    # store/display table values (rounded to three decimal places as necessary)
    print("(" + str(round(x,3)) + "," + str(round(y,3)) + ")")


    i = i+1
    