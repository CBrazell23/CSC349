def singleton(arr):
  mid = (len(arr)//2)
  leftHalf = arr[:mid]
  rightHalf = arr[mid:len(arr) - 1]

  return merge(singleton(leftHalf), singleton(rightHalf), leftHalf, rightHalf)

def merge(left_A, right_A, leftHalf, rightHalf):
    result = []
    for x in left_A:
      if(x != right_A[0]):
        result.append(x)
    
    for x in right_A:
      if(x != left_A[len(left_A) - 1]):
        result.append(x)
    
    return result

arr = [-2, -2, 5, 5,12,12,67,67,72,80,80]
print(singleton(arr))