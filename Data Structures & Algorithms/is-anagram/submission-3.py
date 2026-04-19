class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = defaultdict(int)
        tMap = defaultdict(int)

        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1

        return sMap == tMap