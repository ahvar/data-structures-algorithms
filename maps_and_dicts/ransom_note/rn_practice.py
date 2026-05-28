from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = Counter(magazine)
        for char in ransomNote:
            if mag_letters.get(char, 0) == 0:
                return False
            mag_letters[char] -= 1
        return True


class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    def test_solution(self):
        assert self.solution.canConstruct(ransomNote="aa", magazine="aab") == True
