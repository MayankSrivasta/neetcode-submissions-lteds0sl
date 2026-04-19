class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)

        s1Count = Counter(s1)
        s2Count = Counter(s2[: n - 1])

        i = 0
        for j in range(n - 1, m):
            s2Count[s2[j]] += 1

            if s1Count == s2Count:
                return True
            
            s2Count[s2[i]] -= 1
            i += 1
        
        return False





