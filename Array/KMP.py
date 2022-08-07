class KMP:
    def __init__(self, pat, txt):
        self.pat = pat
        self.txt = txt

        self.KMP()

    def KMP(self):
        pat = self.pat
        M = len(pat)

        dp = [[0 for _ in range(256)] for _ in range(M)]

        dp[0][ord(pat[0])-ord('a')] = 1
        X = 0
        for j in range(1, M):
            for c in range(256):
                if ord(pat[j])-ord('a') == c:
                    dp[j][c] = j+1
                else:
                    dp[j][c] = dp[X][c]

            X = dp[X][ord(pat[j])-ord('a')]
        self.dp = dp

    def search(self):
        txt = self.txt
        dp = self.dp
        M = len(self.pat)
        N = len(self.txt)
        j = 0
        for i in range(1,N):
            j = dp[j][ord(txt[i])-ord('a')]
            if j==M:
                return i-M+1
        return -1

if __name__ == "__main__":
    s = KMP('aba','aabab')
    print(s.search())