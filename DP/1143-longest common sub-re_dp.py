

class Solution:
    def longestCommonSubsequence(self, text1,text2) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        res = 0
        ##Base case dp[0][0] = 0
        ## re dp alogo
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])

            res = max(res, max(dp[i]))

        print(dp)
        return res

    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        global memo
        memo = [[-1] * n for _ in range(m)]
        return self.dp(text1, 0, text2, 0)

    def dp(self, s1, i, s2, j):
        if i == len(s1) or j == len(s2):
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        if s1[i] == s2[j]:
            memo[i][j] = 1 + self.dp(s1, i + 1, s2, j + 1)

        else:
            memo[i][j] = max(self.dp(s1, i + 1, s2, j),
                             self.dp(s1, i, s2, j + 1))
        print(memo)
        return memo[i][j]





if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonSubsequence2("abcde","ace"))
    # print(s.longestCommonSubsequence("abc", "abc"))
    # print(s.longestCommonSubsequence("abc", "def"))
    # print(s.longestCommonSubsequence("ezupkr", "ubmrapg"))
    # print(s.longestCommonSubsequence("bmwgrm", "bmmlsg"))