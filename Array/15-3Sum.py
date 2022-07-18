class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            res = self.twoSum(nums[i+1:],-nums[i])
            for lst in res:
                lst.append(nums[i])
                ans.append(lst)

        return ans

    def twoSum(self, nums, target):
        l= 0
        r = len(nums)-1
        res = []
        while l<r:
            sum = nums[l]+nums[r]
            left,right = nums[l],nums[r]
            if sum<target:
                while l<r and nums[l]==left:
                    l+=1
            if sum>target:
                while l < r and nums[r] == right:
                    r-=1
            if sum==target:
                res.append([left, right])
                while l<r and nums[l]==left:
                    l+=1
                while l < r and nums[r] == right:
                    r-=1

        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,-2,-1]
    i = s.threeSum(nums)
    print(i)
