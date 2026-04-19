class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        n = len(nums)
        arr = [1] * n
        
        for i in range(n):
            arr[i] = left
            left *= nums[i]

        for i in range(n - 1, -1, -1):
            arr[i] *= right
            right *= nums[i]
        
        return arr
