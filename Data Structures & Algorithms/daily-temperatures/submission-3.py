class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temp)

        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res