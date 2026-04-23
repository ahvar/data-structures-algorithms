class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])

    def reverse_words_pythonic(self, s):
        pass

    def reverse_in_place(self, s: str):
        right = len(s) - 1
        reversed_words = []
        while right >= 0:
            while right >= 0 and s[right] == " ":
                right -= 1

            if right < 0:
                break

            left = right

            while left >= 0 and s[left] != " ":
                left -= 1

            reversed_words.append(s[left + 1 : right + 1])
        " ".join(reversed_words)


class TestSolution:

    def setup_method(self):
        self.solution = Solution()

    def test_reverseWords(self):
        assert self.solution.reverseWords("the sky is blue") == "blue is sky the"

    def test_reverse_in_place(self):
        assert self.solution.reverse_in_place("the sky is blue") == "blue is sky the"
