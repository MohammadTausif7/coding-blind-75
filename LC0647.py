class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def expand(i: int, j: int):
            nonlocal count

            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1

        for m in range(len(s)):
            expand(m, m)
            expand(m, m + 1)

        return count
