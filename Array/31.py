


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                # get the index before the last peak
                j = i - 1
                for k in range(i, len(nums)):
                    if nums[j] < nums[k]:
                        nums[k], nums[j] = nums[j], nums[k]
                        return nums
        return nums.reverse()




if __name__ == "__main__":
    s = Solution()
    nums = [1,5,8,6,7,3,2,1]
    i = s.nextPermutation(nums)
    print(i)
