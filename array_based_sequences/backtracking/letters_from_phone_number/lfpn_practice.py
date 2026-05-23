from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        output = []

        def backtrack(path, index):
            if index == len(digits):
                output.append("".join(path))
                return

            for c in phone[digits[index]]:
                path.append(c)
                backtrack(path, index + 1)
                path.pop()

        backtrack(digits, 0)
