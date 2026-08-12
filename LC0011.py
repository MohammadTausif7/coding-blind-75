class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxwater = 0

        while left < right:
            width = right - left
            hght = min(height[left], height[right])
            area = width * hght

            maxwater = max(maxwater, area)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return maxwater