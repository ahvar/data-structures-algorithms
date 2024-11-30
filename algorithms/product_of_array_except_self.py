"""
238
PRODUCT OF ARRAY EXCEPT SELF
----------------------------
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List
from functools import reduce
import operator
import numpy as np


def product_of(nums: List):
    i = 0
    answer = []
    while i in range(0, len(nums)):
        if i == 0:
            a, *b = nums[i:]
            answer.append(np.prod(b))
        elif i == len(nums) - 1:
            *a, b = nums[0 : len(nums)]
            answer.append(np.prod(b))
        elif 0 < i:
            a, *b = nums[i:]
            c, *d = nums[0:i]
            suffix_product = np.prod(b)
            prefix_product = np.prod(d)
            answer.append(suffix_product * prefix_product)
        i += 1
    return answer


if __name__ == "__main__":

    nums = [1, 2, 3, 4]
    more_nums = [-1, 1, 0, -3, 3]
    print(product_of(nums))
