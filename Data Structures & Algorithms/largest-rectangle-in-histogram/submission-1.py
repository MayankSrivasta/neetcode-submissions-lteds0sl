class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []            # (index, height)
        heights.append(0)     # sentinel
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, v = stack.pop()
                w = i - idx
                maxArea = max(maxArea, v * w)
                start = idx
            stack.append((start, h))
        return maxArea