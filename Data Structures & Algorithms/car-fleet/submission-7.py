class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            val = (target - p) / s

            if stack and stack[-1] >= val:
                continue
            else:
                stack.append(val)



        return len(stack)