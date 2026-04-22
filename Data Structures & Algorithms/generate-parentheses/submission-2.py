class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def genPar(open, close):
            if open == close == n:
                res.append("".join(stack))
                return
            
            if n > open:
                stack.append("(")
                genPar(open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(")")
                genPar(open, close + 1)
                stack.pop()
        
        genPar(0, 0)
        return res