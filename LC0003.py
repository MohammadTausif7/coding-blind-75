class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastseen = {}
        i = 0
        maxlen = 0

        for j, char in enumerate(s):
            if char in lastseen and lastseen[char] >= i:
                i = lastseen[char] + 1
            
            lastseen[char] = j
            maxlen = max(maxlen, j - i + 1)

        return maxlen