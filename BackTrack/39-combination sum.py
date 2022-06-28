class Solution:
    def combinationSum(self, candidates, target):
        res = []
        self.dfs(candidates,target, [], res)
        return res


    def dfs(self, candidates, target, path, res):
        if sum(path) == target:
            res.append(path)
        if sum(path) > target:
            return
        for i in range(len(candidates)):
            path_ = path + [candidates[i]]
            candidates_ = candidates[i:]
            self.dfs(candidates_, target, path_, res)


if __name__=="__main__":
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    r = s.combinationSum(candidates, target)
    print(r)
