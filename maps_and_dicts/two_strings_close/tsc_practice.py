class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        f1 = {}
        f2 = {}
        for c in word1:
            f1[c] = f1.get(c, 0) + 1

        for c in word2:
            f2[c] = f2.get(c, 0) + 1

        vals1 = sorted(f1.values())
        vals2 = sorted(f2.values())

        return vals1 == vals2


if __name__ == "__main__":
    word1 = "abc"
    word2 = "bca"
    solution = Solution()
    solution.closeStrings()
