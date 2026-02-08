"""
A phrase is a palindrome if, after converting all uppercase
letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def _clean_string(s):
        n = len(s)
        return n, "".join([char for char in s if char.isalnum()])

    def is_palindrome_two_pointer(self, s: str) -> bool:
        n, clean = self._clean_string(s)
        right = len(s) - 1
        for left in range(len(s)):
            if left > right:
                return True
            if not s[left].isalnum():
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            right -= 1

    def isPalindrome(self, s: str) -> bool:
        n, clean = self._clean_string(s)
        if n == 0:
            return False
        if n == 1 and s.isalpha():
            return True
        print(clean.lower())
        print(clean[::-1].lower())
        return clean.lower() == clean[::-1].lower()


if __name__ == "__main__":
    string = "0P"
    solution = Solution()
    print(solution.isPalindrome(string))
