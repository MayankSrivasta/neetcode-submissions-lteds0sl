class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, v1 in enumerate(words):
            for j, v2 in enumerate(words):
                if i != j and v1 in v2:
                    res.append(v1)
                    break
        return res