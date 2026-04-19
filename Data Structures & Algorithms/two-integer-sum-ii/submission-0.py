class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l = 0
        r = len(num) - 1
        while l < r:
            currSum = num[l] + num[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]