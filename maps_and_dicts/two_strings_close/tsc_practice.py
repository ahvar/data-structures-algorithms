from collections import Counter


class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        word1_count = Counter(word1)
        word2_count = Counter(word2)

        vals1 = sorted(word1_count.values())
        vals2 = sorted(word2_count.values())

        return vals1 == vals2


if __name__ == "__main__":
    word1 = "abc"
    word2 = "bca"
    solution = Solution()
    solution.closeStrings()
