class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        i = 0
        maxfreq = 0
        result = 0

        for j in range(len(s)):
            char = s[j]
            count[char] = count.get(s[j], 0) + 1
            maxfreq = max(maxfreq, count[char])

            while (j - i + 1) - maxfreq > k:
                count[s[i]] -= 1
                i += 1

            result = max(result, j - i + 1)

        return result