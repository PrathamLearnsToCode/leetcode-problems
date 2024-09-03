class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        mini = prices[0]
        for i in range(1,n):
            cost = prices[i] - mini
            profit = max(cost,profit)
            mini = min(mini, prices[i])
            
        return profit
        