class Solution:
    # requiement: O(log n)
    # try double points
    def searchRange(self, nums, target) -> int:
        if len(nums) == 0:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        while left< right:
            



if __name__ =="__main__":
    s = Solution()
    nums = [1,1,1,2,2,3]
    i = s.searchRange(nums, 2)
    print(nums[:i])
