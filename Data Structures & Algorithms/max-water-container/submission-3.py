class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            if heights[l] < heights[r]:
                h = heights[l]
                water = max(water, (r - l) * h)
                l += 1
            else:
                h = heights[r]
                water = max(water, (r - l) * h)
                r -= 1
        return water