char = 65
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
  for j in range(i):
    print(chr(char), end="")
    char += 1
    if char > 90:
      char = 65
  print()