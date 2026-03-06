class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        for c in magazine:
            mag_letters[c] = mag_letters.get(c, 0) + 1
        for c in ransomNote:
            if c not in mag_letters or mag_letters[c] == 0:
                return False
            mag_letters[c] -= 1
        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    print(solution.canConstruct(ransomNote, magazine))
