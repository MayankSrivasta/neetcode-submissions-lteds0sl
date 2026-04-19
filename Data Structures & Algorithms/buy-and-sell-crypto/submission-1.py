class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        n = len(prices)
        for r in range(1,n):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
        return res