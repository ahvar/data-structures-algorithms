DESCRIPTION (inspired by Leetcode.com)

Given a source string s1 and a pattern string s2, find the shortest
contiguous portion of s1 that contains s2 as a subsequence.

Return the shortest such substring. If no valid substring exists, return
an empty string.

When multiple substrings of equal minimum length exist, return the one that
appears first (leftmost).

Reminder: A subsequence maintains the relative order of characters but
doesn't require them to be consecutive.

Example 1

Input:

s1 = "hellointerview"
s2 = "her"
Output:

"hellointer"
Explanation: We need 'h' → 'e' → 'r' in order. The shortest window containing this subsequence starts at 'h' (index 0), includes 'e' (index 1), and ends at 'r' (index 9), giving us "hellointer".

Example 2

Input:

s1 = "codingisfun"
s2 = "xyz"
Output:

""
Explanation: None of the characters 'x', 'y', or 'z' appear in s1, so no valid subsequence window exists.