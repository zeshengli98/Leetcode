class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = [1]*n
        ## Base case
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)

if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    i = s.maxSubArray(nums)
    print(i)
