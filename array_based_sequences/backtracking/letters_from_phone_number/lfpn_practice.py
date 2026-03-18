from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return
        result = []
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

        def backtrack(path, index):
            if index == len(digits):
                result.append("".join(path))
                return
            for char in phone[digits[index]]:
                path.append(char)
                backtrack(path, index + 1)
                path.pop()

        backtrack([], 0)
        return result
