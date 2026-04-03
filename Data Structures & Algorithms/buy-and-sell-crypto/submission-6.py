class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        lo = 0
        max_profit = 0
        for i in range(1, n):
            sell = prices[i]
            buy = prices[lo]
            max_profit = max(max_profit, sell - buy)
            if sell < prices[lo]:
                lo = i
        return max_profit