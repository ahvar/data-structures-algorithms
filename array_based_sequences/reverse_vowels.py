"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"


"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        slist = list(s)
        vowel_indexes = []
        for i in range(len(s)):
            if s[i].lower() in ["a", "e", "i", "o", "u"]:
                vowel_indexes.append(i)
        left = 0
        right = len(vowel_indexes) - 1
        while left < right:
            slist[vowel_indexes[left]], slist[vowel_indexes[right]] = (
                slist[vowel_indexes[right]],
                slist[vowel_indexes[left]],
            )
            left += 1
            right -= 1
        print(vowel_indexes)
        return "".join(slist)

    def reverse_with_stack(self, s: str) -> str:
        vowel_stack = []
        vowels = ["a", "e", "i", "o", "u"]
        slist = list(s)
        for i in range(len(slist)):
            if slist[i].lower() in vowels:
                vowel_stack.append(s[i])
        for i in range(len(slist)):
            if slist[i].lower() in vowels:
                slist[i] = vowel_stack.pop()
        return "".join(slist)


if __name__ == "__main__":
    s = "leetcode"
    solution = Solution()
    print(solution.reverse_with_stack(s))
