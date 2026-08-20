class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        wordbreak = [False] * (len(s) + 1)
        wordbreak[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if wordbreak[j] and s[j : i] in words:
                    wordbreak[i] = True
                    break
        
        return wordbreak[len(s)]