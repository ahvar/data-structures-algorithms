"""
Find the longest substring of X that is also a subsequence of Y:

X = 'acetucpa'
Y = 'raatucrac'

Compare the running time of two different implementations: a so-called "brute force" solution
with a dynamic programming one.
"""

class Solution:
    def _length(self,substring):
        return len(substring)
    def brute_force(self,x,y):
        """
        1. find all substrings in X; put in list
        2. sort by length
        3. iterate beginning with longest
        4. check if substring is a subsequence of Y
        """
        subs = []
        for i in range(len(x)):
            for j in range(i,len(x)):
                subs.append(x[i:j])
        subs.sort(key=self._length)
        subs.reverse()
        for sub in subs:
            if len(sub) >= 1:
                i = j = 0
                while i < len(sub) and j < len(y):
                    if sub[i] == y[j]:
                        i += 1
                    j += 1
                if i == len(sub):
                    return sub
        return ""

    def dp(self,x,y):
        """
        1. construct dp table
        2. fill table with values
        3. take max
        """
        n, m = len(x), len(y)
        dp = [[0] * len(m+1) for _ in range(n+1)]
        max_len = 0
        end_i = 0
        for i in range(1,n):
            for j in range(1,y):
                if x[i] == y[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                elif x[i] != y[j]:
                    dp[i][j] = dp[i][j-1]

            if dp[i][j] > max_len:
                max_len = dp[i][j]
                end_i = i
        return dp[n][m]
        

if __name__ == "__main__":
    x =  'acetucpa'
    y = 'raatucrac'
    solution = Solution()
    print(solution.brute_force(x,y))
    print(solution.dp(x,y))
