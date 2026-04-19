class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if height[l] < height[r]:
                if leftMax < height[l]:
                    leftMax = height[l]
                else:
                    water += leftMax - height[l]
                l += 1
            else:
                if rightMax < height[r]:
                    rightMax = height[r]
                else:
                    water += rightMax - height[r]
                r -= 1
        return water