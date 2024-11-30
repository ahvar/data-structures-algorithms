"""
Problem Statement:
Given a string s and an integer k, find the length of the longest substring with at most k distinct characters.
"""


class Solution:

    def longest_substring(self, s: str, k: int) -> int:
        freq = {}
        start = 0
        end = 0
        max_window_len = 0
        while end < len(s):
            if start == 0 and end == 0:
                freq[s[start]] = 1
                end += 1
                max_window_len = 1
            elif s[end] not in freq:
                freq[s[end]] = 1
            else:
                freq[s[end]] += 1
                start += 1
            if len(freq.keys()) <= k:
                end += 1
            elif len(freq.keys()) > k:
                start += 1
            max_window_len = max(max_window_len, end - start)


if __name__ == "__main__":
    s = Solution()
    print(s.longest_substring("erruvae", 3))
