class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        self.dfs(nums,[], res)
        return res

    def dfs(self,nums,path,res):
        if len(nums)==0:
            res.append(path)


        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            path_ = path + [nums[i]]
            nums_ = nums[:i] + nums[i+1:]
            self.dfs(nums_, path_, res)

if __name__=="__main__":
    s = Solution()
    nums = [1,1,3]
    r = s.permuteUnique(nums)
    print(r)
