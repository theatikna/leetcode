class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        for i in s:
            hash[i] = hash.get(i,0)+1
        for index, char in enumerate(s):
            if hash[char] == 1:
                return index
        return -1
