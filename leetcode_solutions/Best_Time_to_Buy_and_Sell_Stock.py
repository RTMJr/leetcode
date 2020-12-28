class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        max_profit = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
            
        return max_profit
