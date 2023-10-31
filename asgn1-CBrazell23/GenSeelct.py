from random import seed
from random import randint
import time
from GenerateHelper import SelectionSort

# seed random number generator
seed(232321)
# generate some integers

arr = []
for i in range(5000, 10000, 10):
    for j in range(i):
        value = randint(0, 65535)
        arr.append(value)
    st = time.perf_counter()
    SelectionSort(arr)
    et = time.perf_counter()
    elapsed_time = et - st
    print(elapsed_time)

    arr = []