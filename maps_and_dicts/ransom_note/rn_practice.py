from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        for c in magazine:
            mag_letters[c] = mag_letters.get(c, 0) + 1
        for c in ransomNote:
            if c not in mag_letters or mag_letters.get(c) == 0:
                return False
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_canConstruct(self):
        assert self.solution.canConstruct(ransomNote="aa", magazine="aab") == True
