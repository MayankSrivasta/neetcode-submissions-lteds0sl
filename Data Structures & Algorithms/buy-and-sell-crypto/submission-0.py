class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        maxProfit = 0
        for j in range(len(prices)):
            if prices[i] < prices[j]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
            else:
                i = j
        return maxProfit

