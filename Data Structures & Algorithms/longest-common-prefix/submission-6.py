class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for w in strs[1:]:
                if i >= len(w) or w[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]