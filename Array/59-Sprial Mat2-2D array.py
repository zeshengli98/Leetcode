class Solution:
    def generateMatrix(self, n):
        mat = [[0 for _ in range(n)] for _ in range(n)]

        lower, upper, left, right = n-1, 0, 0, n-1
        num=1
        while num<=n*n:
            if upper<=lower:
                for i in range(left, right+1):
                    mat[upper][i] = num
                    num+=1
                upper+=1

            if right>=left:
                for i in range(upper, lower+1):
                    mat[i][right] = num
                    num+=1
                right-=1

            if lower>=upper:
                for i in range(right, left-1, -1):
                    mat[lower][i] = num
                    num+=1
                lower-=1

            if left<=right:
                for i in range(lower, upper-1,-1):
                    mat[i][left] = num
                    num+=1
                left+=1
        return mat







if __name__ == "__main__":
    s = Solution()
    n = 3
    i = s.generateMatrix(n)
    print(i)
