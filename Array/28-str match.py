class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)

        for i in range(n, len(haystack)+1):
            if haystack[i-n:i] == needle:
                return i-n
        return -1

if __name__ == "__main__":
    s = Solution()
    i = s.strStr('a','a')
    print(i)
