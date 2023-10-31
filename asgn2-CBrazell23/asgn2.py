import sys

def binUniqueSearch(arr):
  mid = len(arr) // 2

  if (len(arr) == 1):
    return arr[0]

  elif(mid % 2 == 1):
    if(arr[mid] == arr[mid - 1]):
      return binUniqueSearch(arr[mid + 1:])

    else:
      return binUniqueSearch(arr[:mid])

  else:
    if(arr[mid] == arr[mid + 1]):
      return binUniqueSearch(arr[mid + 2:])

    else:
      return binUniqueSearch(arr[:mid + 1])
    

fileToRead = sys.argv[1]
f = open(fileToRead, "r")
numbers = []
for line in f:
  numbers.append(line)

print(binUniqueSearch(numbers))