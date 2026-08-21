class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robmax(houses):
            rob1 = 0
            rob2 = 0

            for money in houses:
                cur = max(rob2, money + rob1)
                rob1 = rob2
                rob2 = cur
            
            return rob2

        return max(robmax(nums[:-1]), robmax(nums[1:]))