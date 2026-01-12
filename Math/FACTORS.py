# Find all the factors of a given number
# this process seems to be very slow/inefficient for very large numbers

print("FACTORS")
n = int(input("What number would you like to find factors of? "))

print("Finding all factors of {0}...".format(n))

w = n

while w != 0:
  x = int(n/w)
  if x == n/w:
    if x == 1:
      factors = [1]
    else:  
      factors.append(x)
  
  w = w - 1  

y = len(factors) / 2
z = 0
to_say = ""
while y != 1:
  to_say = to_say + "{0} & {1}, ".format(factors[0 + z],factors[-1 - z])
  y = y - 1
  z = z + 1
to_say = to_say + "{0} & {1}".format(factors[0 + z],factors[-1 - z])
print(to_say)
