class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        freq1, freq2 = {}, {}
        for c in word1:
            freq1[c] = freq1.get(c, 0) + 1
        for c in word2:
            freq2[c] = freq2.get(c, 0) + 1
        vals1 = sorted(freq1.values())
        vals2 = sorted(freq2.values())
        return vals1 == vals2


if __name__ == "__main__":
    word1 = "abc"
    word2 = "bca"
    solution = Solution()
    solution.closeStrings()
