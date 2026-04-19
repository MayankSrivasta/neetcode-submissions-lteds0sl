class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {']':'[','}':'{',')':'('}
        
        for s1 in s:
            if s1 in hm:
                if not stack or hm[s1] != stack.pop():
                    return False
            else:
                stack.append(s1)
        
        return len(stack) == 0