class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        water = 0
        while l < r:
            if heights[l] < heights[r]:
                water = max(water, heights[l] * (r - l))
                l += 1
            else:
                water = max(water, heights[r] * (r - l))
                r -= 1
        return water