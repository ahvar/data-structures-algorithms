class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # because signed num cannot be palindrome
            return False

        original = x
        reverse_num = 0
        while x > 0:
            reverse_num += reverse_num * 10 + x % 10
            x //= 10

        return x == reverse_num
