class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        maxCount = 0
        for n in nums:
            count[n] += 1
            if maxCount < count[n]:
                res = n
                maxCount = count[n]
        return res
                