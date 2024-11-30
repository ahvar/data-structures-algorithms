from typing import List, Any, Dict, Tuple, Set
from math import sqrt
from pprint import PrettyPrinter


# write a function that counts vowels in strings
def count_vowels(letters: str) -> int:
    vowels = "aeiou"
    count = 0
    for letter in letters:
        if letter in vowels:
            count += 1
    return count


# given a list of integers, write a function "squares_of_evens(numbers: List[int]) -> List[int]"
# that returns a list containing the squares of all even numbers in the original list
def squares_of_evens(numbers: List[int]) -> List[int]:
    squares = [
        sqrt(num) for num in numbers if num % 2 == 0
    ]  # ---- % "modulus" operator
    return squares


def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    new_dict = {}
    for key, value in d.items():
        new_dict[value] = key

    return new_dict


def swap_pairs(tp: List[Tuple[Any, Any]]) -> List[Tuple[Any, Any]]:
    new_list = []
    for tpair in tp:
        one, two = tpair
        new_list.append((two, one))
    return new_list


def set_operations(a: Set[int], b: Set[int]) -> Tuple[Set[int], Set[int], Set[int]]:
    return (a | b, a & b, b - a)


def reverse_sublist(lst: List[int], start: int, end: int) -> List[int]:
    sub = lst[start : end + 1]
    sub.reverse()
    return sub


def merge_dicts_unpacking_operator(
    d1: Dict[Any, Any], d2: Dict[Any, Any]
) -> Dict[Any, Any]:
    return {**d1, **d2}


def merge_dicts_bitwise_or(d1: Dict[Any, Any], d2: Dict[Any, Any]) -> Dict[Any, Any]:
    return d1 | d2


def sorting_key(element: Tuple) -> int:
    return element[1]


def sort_by_second_element(tuples: List[Tuple[Any, int]]) -> List[Tuple[Any, int]]:
    tuples.sort(key=sorting_key)
    return tuples


def sort_by_second_element_lambda(
    tuples: List[Tuple[Any, int]]
) -> List[Tuple[Any, int]]:
    tuples.sort(key=lambda element: element[1])
    return tuples


def unique_lengths(strings: List[str]) -> Set[int]:
    lengths = [len(s) for s in strings]
    return set(lengths)


if "__main__" == __name__:
    pp = PrettyPrinter(indent=4)
    # string = "eisjdjeuaolkue"
    # print(count_vowels(string))
    # numbers_list = [1, 3, 6, 7, 2, 89, 4, 99]
    # print(f"sqrt of 6: {sqrt(6)}")
    # print(f"sqrt of 2: {sqrt(2)}")
    # print(f"sqrt of 4: {sqrt(4)}")
    # print(squares_of_evens(numbers_list))
    # tuple_list = [("dog", "cat"), ("tree", "forest"), ("blue", "red")]
    # a = {"four", 8, True, "blue", 3.56}
    # b = {(4, 6), "dog", 0, 12, 1}
    """
    pp.pprint(
        merge_dicts_unpacking_operator(
            {"one": 4, "two": 8, "duck": 9}, {"cow": 5, "duck": 9}
        )
    )
    pp.pprint(
        merge_dicts_bitwise_or({"one": 4, "two": 8, "duck": 9}, {"cow": 5, "duck": 9})
    )
    
    tuples = [
        ("one", 1),
        ("four", 4),
        ("two", 2),
        ("nine", 9),
        ("twelve", 12),
        ("three", 3),
    ]
    pp.pprint(sort_by_second_element_lambda(tuples))
    """
    lengths = ["red", "pup", "blue", "apartment", "kick", "trash", "yellow"]
    pp.pprint(unique_lengths(lengths))
