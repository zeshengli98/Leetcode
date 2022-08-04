from collections import defaultdict
import numpy as np
class Solution:
    def corpFlightBookings(self, bookings, n: int):
        diff = [0 for _ in range(n)]
        for book in bookings:
            i,j = book[0]-1,book[1]-1
            num = book[2]
            diff[i] += num
            if j < n-1:
                diff[j+1] -= num
        return np.cumsum(diff)



if __name__ =="__main__":
    s = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    i = s.corpFlightBookings(bookings,n)
    print(i)
