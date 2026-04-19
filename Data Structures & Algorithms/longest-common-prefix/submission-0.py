class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or strs[0][i] != s[i]:
                    return s[:i]
        return strs[0]