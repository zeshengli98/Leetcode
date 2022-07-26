import numpy as np
class NumArray:

    def __init__(self, nums):
        self.arr = nums

    def sumRange(self, left: int, right: int) -> int:
        presum = np.zeros(len(self.arr)+1)
        for i in range(1,len(presum)):
            presum[i] = presum[i-1] + self.arr[i]
        return presum[-1]

