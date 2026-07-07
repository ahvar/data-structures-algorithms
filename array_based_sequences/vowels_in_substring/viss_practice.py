class Solution:
    def vowelStrings(self, word, queries):
        vowels = set("aeiou")
        n = len(word)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            is_vowel = word[i - 1] in vowels
            prefix_sum[i] = prefix_sum[i - 1] + (1 if is_vowel else 0)

        result = []

        for left, right in queries:
            num_vowels = prefix_sum[right + 1] - prefix_sum[left]
            result.append(num_vowels)
        return result
