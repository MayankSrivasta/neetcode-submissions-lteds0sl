class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {']':'[', '}':'{', ')':'('}
        for s1 in s:
            if stack and s1 in hm:
                if hm[s1] != stack.pop():
                    return False
            else:
                stack.append(s1)
        
        return not stack