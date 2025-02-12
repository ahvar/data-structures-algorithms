from priority_queue import HeapPriorityQueue
from linked_list.positional_list import PositionalList


def key(num):
    return int(num)


def pq_sort(nums):
    n = len(nums)
    p = HeapPriorityQueue()
    for j in range(n):
        element = nums.delete(nums.first())
        p.add(element, element)
    for j in range(n):
        (k, v) = p.remove_min()
        nums.add_last(v)


def pq_sort_alt(nums, key=None):
    """standard approach for customzing the order of a sorting
    algorithm is to provide, as an optional parameter to the sorting
    function, an object that is itself a one-parameter function that computes
    a key for a given element"""
    if key is None:
        key = lambda x: x  # Default key function (identity function)

    n = len(nums)
    p = HeapPriorityQueue()
    for j in range(n):
        element = nums.delete(nums.first())
        p.add(key(element), element)  # Use the key function to compute the key
    for j in range(n):
        (k, v) = p.remove_min()
        nums.add_last(v)


if __name__ == "__main__":
    nums = PositionalList()
    nums.add_first("2")
    nums.add_last("5")
    nums.add_first("3")
    nums.add_first("7")
    pq_sort(nums, key=key)
