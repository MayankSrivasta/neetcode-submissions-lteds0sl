class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        water = 0
        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                water += (leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                water += (rightMax - height[r])
        return water
