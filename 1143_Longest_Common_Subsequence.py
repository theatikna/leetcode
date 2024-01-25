class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # Create a 2D array to store the length of the common subsequence
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the dp array using dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The length of the longest common subsequence is stored in dp[m][n]
        return dp[m][n]

