import sys
import time

# Algorithm from GeeksForGeeks
# https://www.geeksforgeeks.org/python-program-for-selection-sort/


def SelectionSort(selectionArr):
    st = time.perf_counter()
    size = len(selectionArr)
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if selectionArr[j] < selectionArr[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (selectionArr[ind], selectionArr[min_index]) = (selectionArr[min_index], selectionArr[ind])


# Algorithm from GeeksForGeeks
# https://www.geeksforgeeks.org/insertion-sort/


def InsertionSort(insertionArr):
    st = time.perf_counter()
    for i in range(1, len(insertionArr)):
        key = insertionArr[i]

        j = i - 1
        while j >= 0 and key < insertionArr[j]:
            insertionArr[j + 1] = insertionArr[j]
            j -= 1
        insertionArr[j + 1] = key


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# Algorithm from GeeksForGeeks
# https://www.geeksforgeeks.org/python-program-for-merge-sort/


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def convertLineToArr(nums):
    splitNums = nums.split(", ")
    for x in splitNums:
        numbers.append(int(x))


fileToRead = sys.argv[1]
fileToRead = "test_files/" + fileToRead
f = open(fileToRead, "r")
data = f.read()
numbers = []