class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        water = 0
        res = 0
        while l < r:
            water = min(heights[l], heights[r]) * (r - l)
            res = max(res, water)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res