from collections import Counter


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split()
        c2s = {}
        s2c = {}
        for char, word in zip(pattern, words):
            # if the character or word has been mapped
            # and it isn't the
            if (
                c2s.get(char, None) != None
                and c2s.get(char) != word
                or s2c.get(word) != None
                and s2c.get(word) != char
            ):
                return False
            c2s[char] = word
            s2c[word] = char
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.wordPattern(pattern="abba", s="dog cat cat dog") == True
