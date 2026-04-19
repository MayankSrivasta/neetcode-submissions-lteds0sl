class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        sCount = Counter()
        
        l = 0
        minWindow = float('inf')
        ans = ''
        required = len(tCount)
        formed = 0
    
        for r in range(len(s)):

            sCount[s[r]] += 1

            if sCount[s[r]] == tCount[s[r]]:
                formed += 1
            
            # checking
            while required == formed:
                # set ans
                if (r - l + 1) < minWindow:
                    minWindow = (r - l + 1)
                    ans = s[l : r + 1]
                
                # shrink
                sCount[s[l]] -= 1
                if sCount[s[l]] < tCount[s[l]]:
                    formed -=1
                
                l +=1
        return ans