class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = Counter(s1)
        n = len(s1)
        s2Count = Counter(s2[:n - 1])
        s2len = len(s2)
        for r in range(n - 1, s2len):

            s2Count[s2[r]] += 1

            if s1Count == s2Count:
                return True
            
            s2Count[s2[r - n + 1]] -= 1

        return False