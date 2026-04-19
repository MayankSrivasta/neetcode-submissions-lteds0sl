class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        stack = []
        res = [0] * len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        
        return res