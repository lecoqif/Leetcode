class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            minPrice = min(prices[i], minPrice)
            profit = max(profit, prices[i] - minPrice)
        
        return profit