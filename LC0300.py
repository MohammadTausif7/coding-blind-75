class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    sub[i] = max(sub[i], sub[j] + 1)
        
        return max(sub)