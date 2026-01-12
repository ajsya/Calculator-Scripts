# convert angles between degrees and radians (a very pointless program that just presents the built in python functions in a way where it doesn't work half the time) 
from math import *

print("ANGLES")
print("Please choose one of the following:")
print("1. Convert an angle measure from radians to degrees")
print("2. Convert an angle measure from degrees to radians")
selection = input("Please enter your choice (1 or 2): ")
print("")

if selection == "1":
  angleMeasure = input("Please enter the measure of your angle in radians: ")
  print("Converting angle from radians to degrees")
  print(str(degrees(float(angleMeasure))) + " degrees")
elif selection == "2":
  angleMeasure = input("Please enter the measure of your angle in degrees: ")
  print("Converting angle from degrees to radians")
  print(str(radians(float(angleMeasure))) + " radians")
else:
  print("ERROR: Invalid choice! Exiting program...")