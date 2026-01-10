from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        if digits == None or len(digits) == 0:
            return []
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

        def _backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return
            for c in phone[digits[index]]:
                path.append(c)
                _backtrack(index + 1, path)
                path.pop()

        _backtrack(0, [])
        return result


if __name__ == "__main__":
    solution = Solution()
