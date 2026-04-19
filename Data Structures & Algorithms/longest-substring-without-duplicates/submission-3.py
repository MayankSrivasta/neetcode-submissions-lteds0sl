class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hm = {}
        res = 0
        for r, v in enumerate(s):
            if v in hm:
                l = max(l, hm[v] + 1)
            hm[v] = r
            res = max(res, r - l + 1)
        return res

