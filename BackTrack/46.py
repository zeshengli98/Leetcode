class Solution:
    def permute(self, nums):
        ans = []
        self.helper([],nums, ans)
        return ans


    def helper(self, path, nums, ans):
        if len(nums)==0:
            ans.append(path)
            return
        for i in range(len(nums)):
            path1 = path + [nums[i]]
            nums1 = nums[:i]+nums[i+1:]
            self.helper(path1, nums1, ans)

if __name__=="__main__":
    s = Solution()
    nums = [1,2]
    r = s.permute(nums)
    print(r)
