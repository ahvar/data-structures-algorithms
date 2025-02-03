from typing import List


class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """

    def __init__(self):
        self._integers = []

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        self._integers.append(value)

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # TODO: implement this method
        try:
            self._integers.remove(value)
            return True
        except ValueError as ve:
            print(f"{value} not found")
            return False

    def _quicksort(self, arr) -> List:
        if len(arr) < 2:
            return arr
        pivot = arr[len(arr) // 2]
        subarr1 = [i for i in arr if i < pivot]
        subarr2 = [i for i in arr if i > pivot]
        pivots = [i for i in arr if i == pivot]
        return self._quicksort(subarr1) + pivots + self._quicksort(subarr2)

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        # TODO: implement this method
        if not self._integers:
            raise RuntimeError
        sorted_integers = self._quicksort(self._integers)
        mid = len(sorted_integers) // 2
        if len(sorted_integers) % 2 == 0:
            return sorted_integers[mid - 1]
        else:
            return sorted_integers[mid]
