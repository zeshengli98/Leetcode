class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res
    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            path_ = path + [nums[i]]
            nums_ = nums[i+1:]
            self.dfs(nums_, path_, res)

if __name__=="__main__":
    s = Solution()
    nums = [1,2,3]
    r = s.subsets(nums)
    print(r)
