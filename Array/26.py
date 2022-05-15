

class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1
        return j


if __name__ =="__main__":
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    i = s.removeDuplicates(nums)
    print(nums[:i])
