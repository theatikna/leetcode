class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length

        prefixProduct = 1
        for i in range(length):
            products[i] = prefixProduct
            prefixProduct *= nums[i]

        suffixProduct = 1
        for i in range(length - 1, -1, -1):
            products[i] *= suffixProduct
            suffixProduct *= nums[i]

        return products
