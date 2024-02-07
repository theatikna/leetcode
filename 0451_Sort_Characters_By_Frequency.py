from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        counts = Counter(s)
        
        # Sort characters based on their frequency
        sorted_chars = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        
        # Build the resulting string
        res = ''.join(char * counts[char] for char in sorted_chars)
        
        return res
