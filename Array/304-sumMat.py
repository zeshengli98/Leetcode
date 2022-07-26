import numpy as np
class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.preSum = np.zeros((m+1,n+1),dtype=int)
        self.mat = matrix
        for i in range(1, m+1):
            for j in range(1,n+1):
                self.preSum[i][j] = self.preSum[i][j-1] + self.preSum[i-1][j] + self.mat[i-1][j-1] - self.preSum[i-1][j-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.preSum[row2+1][col2+1]-self.preSum[row1][col2+1]-self.preSum[row2+1][col1]+self.preSum[row1][col1]

if __name__ =="__main__":
    nums = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    s = NumMatrix(nums)
    i = s.sumRegion(2,1,4,3)
    print(i)