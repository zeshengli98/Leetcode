class Solution:
    def maxProfit(self,maxk, prices):
        if len(prices)==0:
            return 0
        dp = [[[0,0] for _ in range(maxk+1)] for _ in range(len(prices))]
        for k in range(1, maxk+1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]

        for i in range(1,len(prices)):
            for k in range(1,maxk+1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return max([x[0] for x in dp[-1]])


if __name__ == "__main__":
    s = Solution()
    k=2
    prices = [3,2,6,5,0,3]
    i = s.maxProfit(k,prices)
    print(i)
