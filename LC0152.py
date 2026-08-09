class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentmax = nums[0]
        currentmin = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            if num < 0:
                currentmax, currentmin = currentmin, currentmax
            
            currentmax = max(num, currentmax * num)
            currentmin = min(num, currentmin * num)
            answer = max(answer, currentmax)

        return answer