class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) == 0:
            return True
        mag = {}
        for c in magazine:
            if c not in mag:
                mag[c] = 0
            mag[c] += 1

        for c in ransomNote:
            if c not in mag or mag[c] == 0:
                return False
            mag[c] -= 1
        return True
