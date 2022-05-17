import time

from random import randint, seed

seed(2)

def merge(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


arr = []
for i in range(1, 1001):
    arr.append(randint(-1000, 1000))

print("Given Array is")
a = 0
for i in arr:
    if a == 19:
        print(i)
        a = 0
    else:
        print(i, end=' ')
        a += 1

start_time = time.time()
# Function Call
merge(arr)

print("--- %s seconds ---" % (time.time() - start_time))

print("After Sorting Array is")
a = 0
for i in arr:
    if a == 19:
        print(i)
        a = 0
    else:
        print(i, end=' ')
        a += 1