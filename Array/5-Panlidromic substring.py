

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        ans = ""
        for i in range(len(s) - 1):
            s1 = self.isPalindrome(s, i, i)
            s2 = self.isPalindrome(s, i, i + 1)

            ans = s1 if len(s1) > len(ans) else ans
            ans = s2 if len(s2) > len(ans) else ans
        return ans

    def isPalindrome(self, s, l, r):
        temp = ""

        while l >= 0 and r < len(s) and s[l] == s[r]:
            temp = s[l:r+1]
            l -= 1
            r += 1
        return temp


if __name__ =="__main__":
    s = Solution()
    nums = "a"

    i = s.longestPalindrome(nums)
    print(i)
