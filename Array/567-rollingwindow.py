from collections import defaultdict

class Solution:
    def checkInclusion(self, s1, s2):
        window = defaultdict(lambda:0)
        for i in range(len(s1)):
            window[s1[i]] +=1

        left=0
        right=0
        while right<len(s2):
            window[s2[right]] -=1
            right+=1

            if right - left == len(s1)+1:
                window[s2[left]]+=1
                left+=1

            if any(window.values())==0:
                return True
        return False




if __name__ =="__main__":
    sol = Solution()
    s1 = "ab"
    s2 = "eidboaoo"
    i = sol.checkInclusion(s1,s2)
    print(i)
