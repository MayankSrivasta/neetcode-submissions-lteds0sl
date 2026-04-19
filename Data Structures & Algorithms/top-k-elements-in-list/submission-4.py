class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)

        for v, c in count.items():
            freq[c].append(v)

        res = []
        for j in range(len(freq) - 1, 0, -1):
            for c in freq[j]:
                res.append(c)
                if len(res) == k:
                    return res