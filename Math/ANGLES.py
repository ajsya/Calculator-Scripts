from math import *
print()
while True:
  print("")
  print("1: Degrees to radians")
  x = input("2: Radian to degrees")

  y = input("?")
  y = float(y)
  if x=="1":
    print(radians(y))
  elif x=="2":
    print(degrees(y))
  else:
    print("ERROR")