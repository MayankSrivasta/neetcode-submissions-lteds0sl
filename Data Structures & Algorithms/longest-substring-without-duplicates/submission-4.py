class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hm = {}
        width = 0
        for r, v in enumerate(s):
            if v in hm:
                l = max(l, hm[v] + 1)
            hm[v] = r
            width = max(width, r - l + 1)
        return width

