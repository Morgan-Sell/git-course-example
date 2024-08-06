import numpy as np
import pandas as pd
from typing import List

integers1 = [2, 3, 4, 5]
integers2 = [3, 6, 9]

def concat_two_lists(arr1: List, arr2: List) -> List:
    return integers1 + integers2

def find_max_value(arr: List) -> int:
    return max(arr)

def multiple_arrays(arr1: List, arr2: List) -> List:
    if len(arr1) != len(arr2):
        raise(f"Arrays' length must be equal. \
              arr1: {arr1} \
              arr2: {arr2}")
    else:
        return np.dot(arr1, arr2)

new_arr = concat_two_lists(integers1, integers2)

max_val = find_max_value(new_arr)

print("Max Value: ", max_val)

arr_product = multiple_arrays(integers1, integers2)

print(arr_product)