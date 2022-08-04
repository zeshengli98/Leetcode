from collections import defaultdict
import numpy as np
class Solution:
    def reverseWords(self, s):
        ls = s.split(" ")
        ls = [v for v in ls if v != ""]
        i,j = 0, len(ls)-1
        while i<j:
            ls[i],ls[j] = ls[j],ls[i]
            i+=1
            j-=1

        return  " ".join(ls)


if __name__ =="__main__":
    s = Solution()
    st = "  hello world  "
    i = s.reverseWords(st)
    print(i)
