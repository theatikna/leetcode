class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums)
        duplicate = 0 
        for i in nums:
            if i in hashmap:
                duplicate = i
            else :
                hashmap[i]= i 
        total_error = sum(nums)    #
        total_correct = n * (n+1)//2
        missing = total_correct - total_error + duplicate
        return [duplicate,missing]

