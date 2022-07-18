class Solution:

    def rob_(self, nums):
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1])

    def rob(self, nums) -> int:
        return max(self.rob_(nums[1:]), self.rob_(nums[:-1]))


if __name__ == "__main__":
    s = Solution()
    nums = [0]
    i = s.rob(nums)
    print(i)
