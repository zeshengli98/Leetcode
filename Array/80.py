

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i+=1
            # else:
            #     if nums[i] == nums[j]:
            #         i+=1

        return i


if __name__ =="__main__":
    s = Solution()
    nums = [1,1,1,2,2,3]
    i = s.removeDuplicates(nums)
    print(nums[:i])
