class Solution:
    def combine(self, n,k):
        nums = list(range(1,n+1))
        res = []
        self.dfs(nums, k, [], res)
        return res

    def dfs(self, nums, k, path, res):
        if len(path)==k:
            res.append(path)
        if len(path)>k:
            return
        for i in range(len(nums)):
            path_ = path + [nums[i]]
            nums_ = nums[i+1:]
            self.dfs(nums_, k, path_, res)

if __name__=="__main__":
    s = Solution()
    n = 4
    k = 2
    r = s.combine(n,k)
    print(r)
