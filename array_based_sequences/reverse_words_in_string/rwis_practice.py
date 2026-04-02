class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        result = []
        for w in words:
            w = w.strip()
            result.append(w)
        return " ".join(reversed(result))

    def reverse_words_pythonic(self, s):
        return " ".join(s.split()[::-1])

    def reverse_in_place(self, s: str):
        result = []
        n = len(s)
        right = n - 1
        while right >= 0:
            # skip the spaces
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


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.reverse_in_place("the sky is blue") == "blue is sky the"
