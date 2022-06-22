## Binary Search
### 1. Find a target number in an array:
class Solution:
    # requiement: O(log n)
    # try double points
    def bisearch(self, nums, target) -> int:
        left = 0
        right = len(nums)-1

        while left<=right:
            mid = (right + left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left = mid+1 ## assign left to mid+1 because mid has been checked
            elif nums[mid]>target:
                right = mid-1
        return -1

    ## Above algorithm has drawbacks: we can't get the leftmost and rightmost index
    ## We can use the following algorithm to get the leftmost and rightmost index
    def bisearch_left(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left + right)//2
            if nums[mid]==target:
                right = mid - 1 ## lock the opposite boundary
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if left>=len(nums) or nums[left]!=target: ## check if out of index
            return -1
        return left

    def bisearch_right(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left + right) // 2
            if nums[mid]==target:
                left = mid + 1 ## lock the opposite boundary
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right<0 or nums[right]!=target:
            return -1
        return right

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,2,2,2,2]
    nums2 = [-1,0,3,5,9]
    nums3 = [1,1,1,2,2,2,2,3,3]

    print(s.bisearch_left(nums,2))
    print(s.bisearch_left(nums, 3))
    print(s.bisearch_left(nums2, 3))
    print(s.bisearch_left(nums3, 1))
