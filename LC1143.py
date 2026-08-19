class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)

        sub = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if text1[i] == text2[j]:
                    sub[i][j] = 1 + sub[i + 1][j + 1]
                else:
                    sub[i][j] = max(sub[i + 1][j], sub[i][j + 1])
        
        return sub[0][0]