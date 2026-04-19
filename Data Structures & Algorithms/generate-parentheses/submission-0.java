class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList();
        Stack<Character> stack = new Stack();
        backtrack(n, 0, 0, list, stack);
        return list;
    }

    void backtrack(int n, int open, int close, List<String> list, Stack<Character> stack)
    {
        if(n == close && close == open)
        {
            StringBuilder sb = new StringBuilder();
            for(char ch : stack)
                sb.append(ch);
            list.add(sb.toString());
        }
    

    if(open < n)
    {   
        stack.push('(');
        backtrack(n, open + 1, close, list, stack);
        stack.pop();
    }
    if(close < open)
    {
        stack.push(')');
        backtrack(n, open, close + 1, list, stack);
        stack.pop();
    }
    }
}









