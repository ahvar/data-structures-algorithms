class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        char_index = {}
        word_index = {}

        for index, (char, word) in enumerate(zip(pattern, words)):
            if char_index.setdefault(char, index) != word_index.setdefault(word, index):
                return False
        return True
