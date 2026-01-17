# Generates a table of predicted points using Euler's Method

# imports all the functions in math incase user calls upon them in their dy/dx input
from math import *

# can be called on its own from vars button for quick calculations, or it can be called from main method if user needs guidance on inputs
def euler_method(dydx, n, h, x, y):
    # store/display starting value
    print("Estimated points on equation of line")
    print("(" + str(x) + "," + str(y) + ")")

    # repeat the process of finding x and y values n times
    i = 1
    while i <= n:

        # find y1
        # y1 = y0 + h*(dy/dx)
        slope = eval(dydx)
        y = y + h*(slope)

        # find x1
        # x1 = x0 + h
        x = x + h

        # store/display table values (rounded to three decimal places as necessary)
        print("(" + str(round(x,3)) + "," + str(round(y,3)) + ")  Slope: " + str(round(slope,3)))

        i = i+1

def main():
    print("You must enter dy/dx in terms of how python does math or else you will get an error. \n Ex. 3x^2 + 9(y-1) becomes 3*x**2 + 9*(y-1) \n Basic transcendental functions should work as inputed by the calculator (use buttons). \n x and y must be lowercase.")
    dydx = input("What's the equation of dy/dx?")
    n = int(input("How many steps?"))
    h = float(input("What's the step length"))
    x = float(input("Starting x value"))
    y = float(input("Starting y value?"))

    euler_method(dydx, n, h, x, y)
# does not call the main method for security purposes, but can be selected from the vars button to run independently
