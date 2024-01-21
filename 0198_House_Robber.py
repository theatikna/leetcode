from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        even_sum = 0
        odd_sum = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_sum = max(even_sum + num, odd_sum)
            else:
                odd_sum = max(odd_sum + num, even_sum)

        return max(even_sum, odd_sum)
