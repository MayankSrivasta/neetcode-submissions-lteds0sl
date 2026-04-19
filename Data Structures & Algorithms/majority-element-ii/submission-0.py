class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        div = len(nums) // 3
        res = []
        for num, cnt in count.items():
            if cnt > div:
                res.append(num)
        return res