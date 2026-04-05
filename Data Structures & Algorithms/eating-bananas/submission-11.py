import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p / mid)

            if totalTime <= h:
                r = mid      # ✅ keep mid (it can be answer)
            else:
                l = mid + 1  # ❌ discard mid (too slow)

        return l