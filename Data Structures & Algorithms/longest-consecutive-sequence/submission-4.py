class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for n in hashset:
            if (n - 1) not in hashset:
                l = 1
                while (n + l) in hashset:
                    l += 1
                res = max(res, l)
        return res