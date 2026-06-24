class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])

    def reverse_words_pythonic(self, s):
        pass

    def reverse_in_place(self, s: str):
        result = []
        n = len(s)
        right = n - 1
        while right >= 0:
            while right >= 0 and s[right].isspace():
                right -= 1
            if right < 0:
                break
            left = right
            while left >= 0 and not s[right].isspace():
                left -= 1
            result.append(s[left + 1 : right + 1])
        return " ".join(result)


class TestRWIS:
    def setup_method(self):
        self.solution = Solution()

    def test_rwis(self):
        assert self.solution.reverse_in_place(s="big dog") == "dog big"
