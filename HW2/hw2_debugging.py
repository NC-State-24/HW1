"""
This is python code for merge sort.
"""

import rand


def merge_sort(arr):
    """
    This is function for merge sort
    """
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    This is function for combining results from merge sort to produce sorted array.
    """
    left_index = 0
    right_index = 0
    merge_arr = [0] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]
    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]

    return merge_arr


array_test = rand.random_array([0] * 20)

arr_out = merge_sort(array_test)

print(arr_out)

