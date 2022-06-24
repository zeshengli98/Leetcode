## dp
import numpy as np

## demo
class Solution:
    def fib(self, n):
        memo = np.zeros(n+1)
        return self.helper(memo, n)

    def helper(self, memo, n):
        ##base case
        if n==0 or n==1:
            return n
        ## has been calculated, no need to repeatedly do calculation
        if memo[n]!=0:
            return memo[n]
        memo[n] = self.helper(memo, n-1) + self.helper(memo, n-2)
        return memo[n]


## dp: we can separate the demo to a dp tabel
class Solution2:
    def fib(self, n):
        dp = [0 for _ in range(n+1)]
        ## base case
        dp[0]=0
        dp[1]=1
        # state transition
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

## dp: prune space complexity
class Solution3:
    def fib(self, n):
        if n==0 or n==1:
            return n
        dp = [0 for _ in range(2)]
        ## base case
        dp[0]=0
        dp[1]=1
        # state transition
        for i in range(2,n+1):
            dp_new = dp[1]+dp[0]
            dp[0] = dp[1]
            dp[1] = dp_new

        return dp[-1]







if __name__ == "__main__":
    s = Solution2()
    i = s.fib(20)
    print(i)
