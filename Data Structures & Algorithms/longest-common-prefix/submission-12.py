class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        empty = ""
        for c1 in range(len(strs[0])):
            ch = strs[0][c1]

            for c2 in range(1,n):
                if c1 >= len(strs[c2]) or ch != strs[c2][c1]:
                    return strs[0][:c1]
        return strs[0]