class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        shm = defaultdict(int)
        thm = defaultdict(int)

        if len(s) != len(t):
            return False

        for s1, t1 in zip(s, t):
            shm[s1] += 1
            thm[t1] += 1
            
        return shm == thm