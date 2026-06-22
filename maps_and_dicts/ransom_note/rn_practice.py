from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_letters = Counter(magazine)
        for c in ransomNote:
            if c not in m_letters or m_letters.get(c) == 0:
                return False
            m_letters[c] -= 1
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_cc(self):
        assert self.solution.canConstruct(ransomNote="aa", magazine="aab") == True
