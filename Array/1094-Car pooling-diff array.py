from collections import defaultdict
import numpy as np
class Solution:
    def corpFlightBookings(self, trips, capacity):
        n = max([t[2] for t in trips])
        diff = [0 for _ in range(n)]
        for trip in trips:
            i = trip[1]
            j = trip[2]
            num = trip[0]
            diff[i]+=num
            if j < n:
                diff[j]-=num
        print(np.cumsum(diff))
        if max(np.cumsum(diff))<=capacity:
            return True
        else:
            return False



if __name__ =="__main__":
    s = Solution()
    trips = [[2,1,5],[3,5,7]]
    n = 3
    i = s.corpFlightBookings(trips,n)
    print(i)
