class Solution:
    def moveZeroes(self, nums):
        ## using double points is ez to solve such array questions
        if len(nums)==0:
            return
        slow, fast = 0, 0
        while fast<len(nums):
            if nums[fast]!=0:
                nums[slow], nums[fast]= nums[fast],nums[slow]
                slow+=1
            fast+=1







if __name__ == "__main__":
    s = Solution()
    # nums = [0,1,2,2,3,0,4,2]
    nums = [0,0,1]
    i = s.moveZeroes(nums)
    print(nums)
