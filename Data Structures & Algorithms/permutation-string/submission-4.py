class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1Count = Counter(s1)
        s2Count = Counter(s2[:n - 1])
        l = 0
        for r in range(n - 1, len(s2)):

            s2Count[s2[r]] += 1

            if s2Count == s1Count:
                return True
            
            s2Count[s2[l]] -= 1
            l += 1
        return False
        

            
