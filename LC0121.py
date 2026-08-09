class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minprc = prices[0]
        maxprft = 0

        for price in prices:
            minprc = min(price, minprc)
            maxprft = max(maxprft, price - minprc)

        return maxprft