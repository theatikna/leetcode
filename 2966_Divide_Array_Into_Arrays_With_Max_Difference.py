class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        new = []

        for i in range(0 , len(nums), 3):
            result = nums[i:i+3]
            if max(result) - min(result) <=k :
                new.append(result)
            else :
                return []
        return new
