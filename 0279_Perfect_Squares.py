class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        perfect_squares = [i*i for i in range(1,n+1) if i * i <= n]
        for i in range(1,n+1):
            dp[i] = i
            for square in perfect_squares:
                if i < square:
                    break
                dp[i] = min(dp[i],dp[i - square] + 1)
        return dp[n]
