class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        n = len(s)
        right = n - 1

        while right >= 0:
            while right >= 0 and s[right] == " ":
                right -= 1

            if right < 0:
                break

            left = right

            while left >= 0 and s[left] != " ":
                left -= 1

            result.append(s[left + 1 : right + 1])
            right = left
        return " ".join(result)
