class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = [[] for _ in range(len(nums) + 1)]

        count = Counter(nums)

        for v, c in count.items():
            freq[c].append(v)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res