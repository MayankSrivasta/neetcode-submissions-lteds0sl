class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for j in range(1, len(prices)):
            if prices[j - 1] < prices[j]:
                profit += (prices[j] - prices[j - 1])
        return profit