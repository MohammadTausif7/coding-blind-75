class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ways = [0] * (target + 1)
        ways[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    ways[i] += ways[i - num]
        
        return ways[target]
