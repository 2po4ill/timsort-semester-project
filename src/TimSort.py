import time

from random import randint, seed

seed(2)

MIN_MERGE = 32

def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


# Merge function merges the sorted runs
def merge(arr, l, m, r):
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for x in range(0, len1):
        left.append(arr[l + x])
    for x in range(0, len2):
        right.append(arr[m + 1 + x])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def tim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = min_run
    while size < n:

        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        size = 2 * size


# Driver program to test above function
if __name__ == "__main__":
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
    tim_sort(arr)

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