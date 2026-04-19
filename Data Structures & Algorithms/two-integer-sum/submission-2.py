class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hm:
                return [hm[diff], i]
            hm[v] = i
        return [-1, -1]