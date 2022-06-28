class Solution:
    def combinationSum3(self, k, n):
        res = []
        candidates = list(range(1,10))
        if sum(range(k+1))>n:
            return []
        self.dfs(k,n,candidates,[], res)
        return res

    def dfs(self,k,n,candidates,path,res):
        if len(path) == k and sum(path)==n:
            res.append(path)
        for i in range(len(candidates)):
            path_ = path + [candidates[i]]
            candidates_ = candidates[i+1:]
            self.dfs(k,n,candidates_,path_,res)




if __name__=="__main__":
    s = Solution()
    k=9
    n=45
    r = s.combinationSum3(k, n)
    print(r)
