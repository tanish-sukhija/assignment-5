start = 1
end = 500
for number in range(start, end+1):
  if number % 7 == 0 and number % 11 == 0:
    print(number)