import random
from typing import List
from rich import print as rprint

def make_words() -> List:
    words = []
    word = ""
    for i in range(0,127):
        for i in range(0,4):
            word += chr(random.randint(97,122))
        words.append(word)
        word = ""
    words.sort()
    return words

def binary_search(target: str) -> str:
    sorted_word_array = make_words()
    target_words = []
    left = 0
    right = len(sorted_word_array) - 1
    while left <= right:
        middle = (left + right) // 2
        first = sorted_word_array[middle][0]
        if first == target:
            target_words.append(sorted_word_array.pop(middle))
        elif first > target:
            right = middle - 1 # move immediately before the middle
        else:
            left = middle + 1 # move immediately after the middle
    return target_words



if __name__ == "__main__":
    target = 'u'
    words_starting_with_target = binary_search(target)
    rprint(words_starting_with_target)
    

