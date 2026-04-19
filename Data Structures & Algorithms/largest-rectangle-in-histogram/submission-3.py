class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                indx, val = stack.pop()
                width = i - indx
                res = max(res, val * width)
                start = indx
            stack.append((start, h))
        return res