class Solution:
    def combinationSum2(self, candidates, target) :
        res = []
        candidates.sort()
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, path, res):
        if sum(path) == target:
            res.append(path)
        if sum(path) > target:
            return
        for i in range(len(candidates)):
            if i!=0 and candidates[i] == candidates[i-1]:
                continue
            path_ = path + [candidates[i]]
            candidates_ = candidates[i + 1:]
            self.dfs(candidates_, target, path_, res)


if __name__=="__main__":
    s = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    r = s.combinationSum2(candidates, target)
    print(r)
