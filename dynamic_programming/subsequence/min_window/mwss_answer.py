def min_window(s1, s2):
    # Measure the source and pattern lengths once so the loop bounds stay simple.
    m, n = len(s1), len(s2)

    # Handle the empty-pattern case up front because an empty subsequence is always present.
    if n == 0:
        return ""

    # dp[j] stores the start index of a window ending at the current source position
    # that contains s2[: j + 1] as a subsequence. -1 means no such window exists yet.
    dp = [-1] * n

    # Track the best answer found so far.
    result = ""
    min_len = float("inf")

    # Scan the source string from left to right.
    for i in range(m):
        # Update the pattern matches from right to left so earlier states are not
        # overwritten before they are used by the next pattern character.
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                # A match for the first pattern character starts a new candidate window.
                if j == 0:
                    dp[j] = i
                # Later pattern characters inherit the start index of the previous prefix.
                else:
                    dp[j] = dp[j - 1]

        # If the full pattern has been matched, evaluate the current window.
        if dp[n - 1] != -1:
            start = dp[n - 1]
            length = i - start + 1

            # Keep only a strictly shorter window so ties remain leftmost.
            if length < min_len:
                min_len = length
                result = s1[start : i + 1]

    # Return the shortest valid window, or an empty string if no match was found.
    return result
