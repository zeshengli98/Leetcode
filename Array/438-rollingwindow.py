from collections import defaultdict

class Solution:
    def findAnagrams(self, s, p) -> int:
        left = 0
        right = 0
        ans = []
        window = defaultdict(lambda: 0)
        for i in range(len(p)):
            window[p[i]] += 1

        while right < len(s):
            window[s[right]]-=1
            right+=1

            if right - left == len(p)+1:
                if s[left] in window:
                    window[s[left]]+=1
                    left += 1

            if any(window.values())==0:
                ans.append(left)
        return ans



if __name__ =="__main__":
    sol = Solution()
    s = "abab"
    p = "ab"
    i = sol.findAnagrams(s,p)
    print(i)
