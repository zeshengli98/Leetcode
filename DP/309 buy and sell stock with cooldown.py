class Solution:
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        dp = [[0,0,0] for _ in range(len(prices))] ## 3 states: not hold, cooldown, hold
        dp[0][0] = 0
        dp[0][1] = 0
        dp[0][2] = -prices[0]

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1])
            dp[i][1] = dp[i-1][2]+prices[i]
            dp[i][2] = max(dp[i-1][2],dp[i-1][0]-prices[i])

        return max(dp[-1][:2])



if __name__ == "__main__":
    s = Solution()

    prices = [1,2,3,0,2]
    i = s.maxProfit(prices)
    print(i)
