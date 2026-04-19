class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        i = 0
        res = 0
        for j in range(len(s)):
            if s[j] in map:
                i = max(i, map[s[j]] + 1)
            map[s[j]] = j
            res = max(res, j - i + 1)

        return res