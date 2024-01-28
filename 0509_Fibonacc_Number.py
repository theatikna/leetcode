class Solution:
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0  # Return 0 for non-positive n

        if n == 1:
            return 1  # Special case for n=1

        hashmap = [0] * n
        prev = 0
        prev2 = 1
        result = 0

        for i in range(n):
            if i == 0:
                result = prev
            elif i == 1:
                result = prev2
            else:
                curr = prev + prev2
                prev, prev2 = curr, prev
                result += curr  # Use curr instead of prev to accumulate the sum

        return result
