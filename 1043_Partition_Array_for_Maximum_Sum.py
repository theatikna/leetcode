class Solution:
    def maxSumAfterPartitioning(self,arr, k):
        N = len(arr)

        dp = [0] * (N + 1)

        for start in range(N - 1, -1, -1):
            currMax = 0
            end = min(N, start + k)

            for i in range(start, end):
                currMax = max(currMax, arr[i])
            # Store the maximum of all options for the current subarray.
                dp[start] = max(dp[start], dp[i + 1] + currMax * (i - start + 1))

        return dp[0]
