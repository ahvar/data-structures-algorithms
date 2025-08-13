"""
Given two strings ransomNote and magazine, return true if ransomNote
can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Step 1: Count all occurrences of each letter
        mag_letters = {}
        for letter in magazine:
            if letter not in mag_letters:
                mag_letters.update({letter: 1})
            else:
                mag_letters[letter] += 1
        note_letters = list(ransomNote)
        for k,v in mag_letters.items():
            for _ in range(v):
                try:
                    note_letters.remove(k)
                except ValueError:
                    break
        if note_letters: return False
        return True 

if __name__ == "__main__":
    ransom = "aa"
    magazine = "aab"
    solution = Solution()
    print(solution.canConstruct(ransom, magazine))
