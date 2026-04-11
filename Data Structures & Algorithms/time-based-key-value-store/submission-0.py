from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]

        l, r = 0, len(arr)

        while l < r:
            mid = (l + r) // 2
            if timestamp < arr[mid][0]:
                r = mid          # keep mid
            else:
                l = mid + 1      # discard mid

        # l is first index > timestamp
        if l == 0:
            return ""
        
        return arr[l - 1][1]