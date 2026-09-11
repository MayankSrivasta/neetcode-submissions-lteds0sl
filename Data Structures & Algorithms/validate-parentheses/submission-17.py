class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = { '}' : '{', ')' : '(', ']' : '['}
        for c in s:
            if stack and c in hm:
                if hm[c] != stack.pop():
                    return False
            else:
                stack.append(c)
            
                
        return len(stack) == 0