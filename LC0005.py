class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand(i: int, j: int) -> str:
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            return s[i + 1 : j]
        
        for m in range(len(s)):
            odd = expand(m, m)
            even = expand(m, m + 1)

            if len(odd) > len(result):
                result = odd
            
            if len(even) > len(result):
                result = even

        return result