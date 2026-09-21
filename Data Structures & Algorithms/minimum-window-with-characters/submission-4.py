class Solution:
    def minWindow(self, s: str, t: str) -> str:
       
        tc = Counter(t)
        sc = Counter()

        l = 0

        required = len(tc)
        formed = 0
        minResult = float('inf')
        minString = ""

        for r in range(len(s)):
            sc[s[r]] += 1

            if tc[s[r]] == sc[s[r]]:
                formed += 1


            while required == formed:

                if minResult > (r - l + 1):
                    minResult = (r - l + 1)
                    minString = s[l : (r + 1)]

                sc[s[l]] -= 1

                if sc[s[l]] < tc[s[l]]:
                    formed -= 1

                l += 1
        
        return minString