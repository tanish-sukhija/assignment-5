start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
div = int(input("Enter the number to check divisibility by: "))
for num in range(start, end+1):
  if num % div == 0:
    print(num)