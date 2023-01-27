positives = []
negatives = []
odds = []
evens = []
count = {}
for i in range(10):
  num = int(input("Enter an integer: "))
  if num > 0:
    positives.append(num)
  elif num < 0:
    negatives.append(num)
  if num % 2 == 0:
    evens.append(num)
  else:
    odds.append(num)
  if num in count:
    count[num] += 1
  else:
    count[num] = 1
print("Positive numbers:", *positives)
print("Negative numbers:", *negatives)
print("Odd numbers:", *odds)
print("Even numbers:", *evens)
print("Number count:", count)