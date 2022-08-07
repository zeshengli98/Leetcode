class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        window = {}
        res = ""
        length = float('inf')

        for e in t:
            if e in window.keys():
                window[e] += 1
            else:
                window[e] = 1

        while right < len(s):
            c = s[right]
            if c in window.keys():
                window[c] -= 1

            while all(v <= 0 for v in window.values()):
                if right - left < length:
                    res = s[left:right + 1]
                    length = right - left
                c = s[left]
                if c in window.keys():
                    window[c] += 1
                left += 1
            right += 1

        return res
