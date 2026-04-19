class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)

        for j in range(len(temp)):
            while stack and temp[stack[-1]] < temp[j]:
                b = stack.pop()
                res[b] = j - b
            stack.append(j)
        return res