class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l = 0
        profit = 0
        for r in range(1, len(nums)):
            if nums[l] < nums[r]:
                profit = max(profit, nums[r] - nums[l])
            else:
                l = r
        return profit