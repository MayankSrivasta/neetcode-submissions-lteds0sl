class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shm = {}
        thm = {}

        if len(s) != len(t):
            return False

        for s1, t1 in zip(s, t):
            shm[s1] = shm.get(s1, 0) + 1
            thm[t1] = thm.get(t1, 0) + 1
            
        return shm == thm