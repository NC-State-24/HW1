import pytest
from rand import random_array
from hw2_debugging import merge_sort

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5] but got {sorted_arr}"

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5] but got {sorted_arr}"

def test_array_with_duplicates():
    arr = [2, 4, 3, 4, 1]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 4], f"Expected [1, 2, 3, 4, 4] but got {sorted_arr}"

if __name__ == "__main__":
    pytest.main()