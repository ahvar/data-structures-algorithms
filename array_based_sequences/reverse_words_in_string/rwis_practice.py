class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])

    def reverse_words_pythonic(self, s):
        pass

    def reverse_in_place(self, s: str):
        if not s:
            return ""
        arr = []
        i = len(s) - 1
        while i >= 0:
            if s[i].isspace():
                i -= 1
                continue
            j = i
            while j >= 0 and s[j].isalpha():
                j -= 1
            arr.append(s[j + 1 : i + 1])
            i = j
        return " ".join(arr)


class TestRWIS:
    def setup_method(self):
        self.solution = Solution()

    def test_rwis(self):
        assert self.solution.reverse_in_place(s="big dog") == "dog big"
        assert self.solution.reverse_in_place(s="the sky is blue") == "blue is sky the"
