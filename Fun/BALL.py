a = 0 
while True:
  if a == 31:
    b = 1 
  if a == 0:
    b = 0
  print(" "*a + "0")
  if b == 0:
    a = a+1
  else:
    a = a-1