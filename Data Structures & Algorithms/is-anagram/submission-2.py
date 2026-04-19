class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sChar = defaultdict(int)
        tChar = defaultdict(int)

        for i in range(len(s)):
            sChar[s[i]] += 1
            tChar[t[i]] += 1
        
        return sChar == tChar
