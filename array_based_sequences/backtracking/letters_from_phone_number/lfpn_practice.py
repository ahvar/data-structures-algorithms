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
        result = []

        def backtrack(path, index):
            if index == len(digits):
                result.append("".join(path))
                return
            for char in phone[digits[index]]:
                if char not in path:
                    path.append(char)
                    backtrack(path, index + 1)
                    path.pop()

        backtrack([], 0)
        return result


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_phone(self):
        assert self.solution.letter_combinations(digits="23") == [
            "ad",
            "ae",
            "af",
            "bd",
            "be",
            "bf",
            "cd",
            "ce",
            "cf",
        ]
