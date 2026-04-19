class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        maxL = 0
        for n in hset:
            if (n - 1) not in hset:
                l = 1
                while (n + l) in hset:
                    l += 1
                maxL = max(maxL, l)
        return maxL