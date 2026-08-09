class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vstd = {}

        for i, num in enumerate(nums):
            need = target - num

            if need in vstd:
                return [vstd[need], i]
                
            vstd[num] = i