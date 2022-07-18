class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1])


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,1]
    i = s.rob(nums)
    print(i)
