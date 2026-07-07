class Solution:
    def vowelStrings(self, word, queries):
        # Step 1: Store the vowels in a set for fast membership checks.
        vowels = set("aeiou")

        # Step 2: Create a prefix sum array with one extra slot for the empty prefix.
        prefix_sum = [0] * (len(word) + 1)

        # Step 3: Walk through the string and track how many vowels have appeared so far.
        for i in range(1, len(word) + 1):
            is_vowel = word[i - 1] in vowels
            prefix_sum[i] = prefix_sum[i - 1] + (1 if is_vowel else 0)

        # Step 4: Prepare the output list for the query answers.
        result = []

        # Step 5: Use the prefix sums to get each substring's vowel count in O(1) time.
        for left, right in queries:
            num_vowels = prefix_sum[right + 1] - prefix_sum[left]
            result.append(num_vowels)

        # Step 6: Return the answers in the same order as the queries.
        return result
