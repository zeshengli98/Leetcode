class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1]*n
        ## Base case
        dp[0] = 1
        for i in range(1,n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    i = s.lengthOfLIS(nums)
    print(i)
