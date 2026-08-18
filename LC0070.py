class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        i = 1
        j = 2

        for m in range(3, n + 1):
            cur = i + j
            i = j
            j = cur
        
        return j