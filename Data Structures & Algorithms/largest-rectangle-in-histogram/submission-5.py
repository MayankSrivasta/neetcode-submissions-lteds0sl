class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0
        for indx, val  in enumerate(heights):
            right = indx
            while stack and stack[-1][0] > val:
                val2, indx2 = stack.pop()
                maxArea = max(maxArea, val2 * (indx - indx2))
                right = indx2
            
            stack.append((val, right))
        
        return maxArea