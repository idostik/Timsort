from random import randint, shuffle
from collections import deque

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    for i in range(left + 1, right + 1):
        item = arr[i]
        j = i - 1
        while j >= left and arr[j] > item:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = item

    return arr


def merge(left, right):
    left_pointer = right_pointer = 0
    left_len, right_len = len(left), len(right)
    result = []
    while left_pointer < left_len and right_pointer < right_len:
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    
    result.extend(
        left[left_pointer:] if left_pointer < left_len else right[right_pointer:]
    )
    return result


def tim_sort(arr):
    MIN_RUN = 32
    n = len(arr)

    for i in range(0, n, MIN_RUN):
        run = i + MIN_RUN
        insertion_sort(arr, i, run if run < n - 1 else n - 1)
    
    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = start + size * 2 - 1 
            if end > n - 1:
                 end = n - 1
            
            merged_arr = merge(
                left=arr[start:mid + 1],
                right=arr[mid + 1:end + 1]
            )
            arr[start:start + len(merged_arr)] = merged_arr

        size *= 2
    
    return arr