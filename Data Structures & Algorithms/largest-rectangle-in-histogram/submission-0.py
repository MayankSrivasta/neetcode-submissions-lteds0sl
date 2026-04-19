class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []            # (index, height)
        heights.append(0)     # sentinel
        maxA = 0

        for i, h in enumerate(heights):
            while stack and h < stack[-1][1]:
                idx, height = stack.pop()
                left = stack[-1][0] if stack else -1
                width = i - left - 1
                maxA = max(maxA, width * height)
            stack.append((i, h))

        return maxA
