"""
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character,
and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
"""
class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        freq1, freq2 = {}, {}
        for c in word1:
            freq1[c] = freq1.get(c,0) + 1
        for c in word2:
            freq2[c] = freq2.get(c,0) + 1
        vals1 = sorted(freq1.values())
        vals2 = sorted(freq2.values())
        return vals1 == vals2


if __name__ == "__main__":
    word1 = "abc"
    word2 = "bca"
    solution = Solution()
    solution.closeStrings()