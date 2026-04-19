class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights.append(0)
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, v = stack.pop()
                w = i - index
                res = max(res, v * w)
                start = index
            stack.append((start, h))
        return res