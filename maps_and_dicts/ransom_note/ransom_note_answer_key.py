class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            return True
        magazine_letters = {}
        for letter in magazine:
            if letter not in magazine_letters:
                magazine_letters[letter] = 0
            magazine_letters[letter] += 1

        for letter in ransomNote:
            if letter not in magazine_letters or magazine_letters[letter] == 0:
                return False
            magazine_letters[letter] -= 1
        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    print(solution.canConstruct(ransomNote, magazine))
