class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expctsum = n * (n + 1) // 2
        actualsum = sum(nums)

        missingnum = expctsum - actualsum

        return missingnum