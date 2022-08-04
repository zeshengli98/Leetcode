class Solution:

    def reverse(self, ls):
        i, j = 0, len(ls)-1
        while i<j:
            ls[i], ls[j] = ls[j], ls[i]
            i+=1
            j-=1


    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        #
        for i in range(n):
            self.reverse(matrix[i])
        print(matrix)



if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    i = s.rotate(matrix)
    print(matrix)
