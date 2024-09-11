"""
This is python code to generate random array for input to merge sort
"""

import subprocess

def random_array(arr):
    """
    This is random function to generate random array for input to merge sort
    """
    shuffled_num = None
    for i in range(len((arr))):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
