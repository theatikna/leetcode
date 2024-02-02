class Solution:
    def sequentialDigits(self, low, high):
        result = []
        for i in range(1, 10):
            num = i
            next_digit = i
            while num <= high and next_digit < 10:
                if num >= low:
                    result.append(num)
                next_digit += 1
                num = num * 10 + next_digit
            result.sort()
        return result

low = 1000
high = 13000
sol = Solution()
re = sol.sequentialDigits(low, high)
print(re)
