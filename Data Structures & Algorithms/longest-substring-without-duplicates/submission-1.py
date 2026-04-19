class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        map = {}
        res = 0
        for r in range(len(s)):
            if s[r] in map:
                l = max(map[s[r]] + 1, l)
            map[s[r]] = r
            res = max(res, r - l + 1)
        return res