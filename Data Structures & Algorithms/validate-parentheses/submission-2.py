class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {'}':'{', ')':'(', ']':'[' }
        stack = []
        for c in s:
            if stack and c in closeToOpen:
                if closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False