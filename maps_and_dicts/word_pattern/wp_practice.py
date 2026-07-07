from collections import Counter


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        word_map = {}
        char_map = {}
        for char, word in zip(pattern, s):
            if (
                char in word_map
                and word_map[char] != word
                or word in char_map
                and char_map[word] != char
            ):
                return False
            word_map[char] = word
            char_map[word] = char
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.wordPattern(pattern="abba", s="dog cat cat dog") == True
