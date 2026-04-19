class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        maxCount = 0
        count = Counter(nums)

        for num, cnt in count.items():
            if maxCount < cnt:
                maxCount = cnt
                res = num
        return res
