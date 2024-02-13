from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        r = ""

        def palindrome(char: str) -> str:
            l = len(char)
            if l % 2 == 0:
                if char[:l//2] == char[l-1:l//2-1:-1]:
                    return char
            else:
                if char[:l//2] == char[l-1:l//2:-1]:
                    return char
            return ""

        for char in words:
            if r == "":
                r = palindrome(char)
        return r
