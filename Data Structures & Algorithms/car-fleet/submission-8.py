class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []
        for p, s in pair:
            val = (target - p) / s

            if not stack or stack[-1] < val:
                stack.append(val)
        
        return len(stack)