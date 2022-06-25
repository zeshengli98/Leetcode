class Solution:
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount+1)
        dp[0]=0
        for a in range(1, amount+1):
            for c in coins:
                if a - c < 0:
                    continue
                dp[a] = min(dp[a], 1+dp[a-c])

        return -1 if dp[-1] == amount+1 else dp[-1]

if __name__ == "__main__":
    s = Solution()
    coins = [3,8,9]
    i = s.coinChange(coins, 4)
    print(i)
