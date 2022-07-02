

class Solution:
    def lengthOfLongestSubstring(self, str) -> int:
        left=0
        right=0
        res = 0
        window = {}
        while right < len(str):
            c = str[right]
            right+=1
            if c not in window.keys():
                window[c] = 1
            else:
                window[c]+=1

            while window[c]>1:
                d = str[left]
                left+=1
                window[d]-=1
            res = max(res, right - left)
        return res



if __name__ =="__main__":
    s = Solution()
    st = "abcabcbb"
    i = s.lengthOfLongestSubstring(st)
    print(i)
