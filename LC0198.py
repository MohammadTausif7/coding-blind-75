class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        robhouse = [0] * len(nums)

        robhouse[0] = nums[0]
        robhouse[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            robhouse[i] = max(robhouse[i - 1], nums[i] + robhouse[i - 2])

        return robhouse[-1]