class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        if n > m:
            return False

        s1Count = Counter(s1)
        s2Count = Counter(s2[:n - 1])

        for j in range(n - 1, m):
            s2Count[s2[j]] += 1

            if s1Count == s2Count:
                return True
                
            k = j - n + 1
            s2Count[s2[k]] -= 1

        return False