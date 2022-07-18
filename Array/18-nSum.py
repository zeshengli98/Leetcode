class Solution:
    def nSum(self, n, nums, target):
        nums.sort()
        length = len(nums)
        res = []
        if n < 2 or length < n:
            return res
        if n==2:
            l= 0
            r = len(nums)-1
            while l<r:
                sum = nums[l]+nums[r]
                left,right = nums[l],nums[r]
                if sum<target:
                    while l<r and nums[l]==left: l+=1
                if sum>target:
                    while l < r and nums[r] == right:r-=1
                if sum==target:
                    res.append([left, right])
                    while l<r and nums[l]==left: l+=1
                    while l < r and nums[r] == right: r-=1
        else:
            for i in range(length):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                sub = self.nSum(n-1, nums[i+1:], target-nums[i])
                for arr in sub:
                    arr.append(nums[i])
                    res.append(arr)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1,0,-1,0,-2,2]
    i = s.nSum(4, nums, 0)
    print(i)
