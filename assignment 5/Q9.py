words = input("Enter a list of words separated by space: ").split()
count = {}
for word in words:
  if word in count:
    count[word] += 1
  else:
    count[word] = 1
print("Word count:", count)