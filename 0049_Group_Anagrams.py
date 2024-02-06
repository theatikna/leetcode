class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for char in strs:
            sorted_char = ''.join(sorted(char))
            if sorted_char in hash:
                hash[sorted_char].append(char)
            else:
                hash[sorted_char] = [char]
        return list(hash.values())
        
