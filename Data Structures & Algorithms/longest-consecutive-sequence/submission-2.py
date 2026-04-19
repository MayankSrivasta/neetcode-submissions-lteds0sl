class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashset = set(nums)
        for n in hashset:
            if (n - 1) not in hashset:
                l = 1
                while (n + l) in hashset:
                    l += 1
                longest = max(l, longest)    
        return longest