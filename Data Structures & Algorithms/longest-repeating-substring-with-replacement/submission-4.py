class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)  # Automatically initializes missing keys to 0
        width = 0
        max_freq = 0
        l = 0

        for r, char in enumerate(s):
            count[char] += 1
            max_freq = max(max_freq, count[char])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            width = max(width, r - l + 1)

        return width