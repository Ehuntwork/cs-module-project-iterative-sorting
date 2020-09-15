def linear_search(arr, target):
    for i in range(0, len(arr)):
        if target == arr[i]:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
import math
def binary_search(arr, target):
    low_position = 0
    high_position = len(arr) - 1

    while low_position <= high_position:
        mid_way = (low_position + high_position) // 2

        if arr[mid_way] == target:
            return mid_way

        if arr[mid_way] < target:
            low_position = mid_way + 1

        else:
            high_position = mid_way - 1

    return -1  # not found
