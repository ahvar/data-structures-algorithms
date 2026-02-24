class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        for letter in magazine:
            mag_letters[letter] = mag_letters.get(letter, 0) + 1
        for letter in ransomNote:
            if letter not in mag_letters or mag_letters[letter] == 0:
                return False
            mag_letters[letter] -= 1
        return True


class TestRansomNote:

    def setup_method(self):
        self.solution = Solution()
        self.ransomeNote = "a"
        self.magazine = "b"

        self.ransomeNote1 = "aa"
        self.magazine1 = "ab"

        self.ransomeNote2 = "aa"
        self.magazine2 = "aab"

    def test_can_construct(self):
        assert self.solution.canConstruct(self.ransomeNote, self.magazine) == False
        assert self.solution.canConstruct(self.ransomeNote1, self.magazine1) == False

        assert self.solution.canConstruct(self.ransomeNote2, self.magazine2) == True
