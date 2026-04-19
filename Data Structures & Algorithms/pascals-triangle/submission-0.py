class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rectangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = rectangle[i - 1][j - 1] + rectangle[i - 1][j] 
            rectangle.append(row)
        return rectangle