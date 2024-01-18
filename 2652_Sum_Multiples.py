class Solution:
    def sumOfMultiples(self, n: int) -> int:
        poss = []
        for i in range(3, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                poss.append(i)
        return sum(poss)
