class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for x in range(1, len(prices)):
            if result < max(prices[x:]) - min(prices[:x]):
                result = max(prices[x:]) - min(prices[:x])
                
        return result