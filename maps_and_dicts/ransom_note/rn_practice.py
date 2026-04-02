class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for c in magazine:
            mag[c] = mag.get(c, 0) + 1
        for c in ransomNote:
            if c not in mag or mag[c] == 0:
                return False
            mag[c] -= 1
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_examples(self):
        assert self.solution.canConstruct("a", "b") == False
        assert self.solution.canConstruct("aa", "ab") == False
        assert self.solution.canConstruct("aa", "aab") == True
