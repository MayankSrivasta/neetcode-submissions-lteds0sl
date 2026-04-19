class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {']':'[','}':'{',')':'('}
        
        for c in s:
            if stack and c in hm:
                    if hm[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(c)
        return not stack