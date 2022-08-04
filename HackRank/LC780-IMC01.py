class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int):
        res = []
        self.dfs(sx,sy,tx,ty,res)
        if len(res)>0:
            return True
        else:
            return False

    def dfs(self, sx, sy, tx, ty, res):
        if sx>tx or sy>ty:
            return
        
        if sx==tx and (ty-sy)%sx==0:
            res.append(True)
            return
        elif sy==ty and (tx-sx)%sy == 0:
            res.append(True)


        if tx>ty:
            self.dfs(sx,sy, tx%ty,ty, res)
        else:
            self.dfs(sx,sy, tx,ty%tx, res)



if __name__ == "__main__":
    s = Solution()
    i=s.reachingPoints(3, 7, 3, 4)
    print(i)
