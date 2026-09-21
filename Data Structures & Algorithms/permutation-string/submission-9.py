class Solution:
# FIXED SIZE SLIDING WINDOW
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hm = Counter(s1)
        n = len(s1)
        
        l = 0
        s2hm = Counter(s2[:n - 1])

        for r in range(n - 1, len(s2)):

            s2hm[s2[r]] += 1

            if s1hm == s2hm:
                return True
            
            s2hm[s2[l]] -= 1
            l += 1

        return False