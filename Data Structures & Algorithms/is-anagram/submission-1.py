class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        sMap, tMap = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1
        return sMap == tMap