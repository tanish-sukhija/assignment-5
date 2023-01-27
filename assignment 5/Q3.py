import math
a = float(input("Enter the side a: "))
b = float(input("Enter the side b: "))
c = float(input("Enter the side c: "))
if a + b > c and a + c > b and b + c > a:
  s = (a + b + c) / 2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  print("The area of the triangle is", area)
else:
  print("The combination of sides is not possible.")