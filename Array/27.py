class Solution:
    def removeElement(self, nums, val):
        ## using double points is ez to solve such array questions
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i] = nums[j]
                i+=1
        return i






if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    i = s.removeElement(nums, 2)
    print(nums[:i])
