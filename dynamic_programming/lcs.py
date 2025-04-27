class LongestCommonSubsequence:
    def __init__(self, str1: str, str2: str):
        self.A = str1
        self.B = str2
        self.dp = [[]]

    def recursion(self, n=0, m=0):
        if n == len(self.A) or m == len(self.B):
            return 0
        elif self.A[n] == self.B[m]:
            return 1 + self.recursion(n + 1, m + 1)
        else:
            return max(
                self.recursion(n + 1, m), self.recursion(n, m + 1)
            )

    def memo(self):
        n = len(self.A)
        m = len(self.B)

        dp = [[-1 for j in range(m)] for i in range(n)]

        return self.__memoUtil(n - 1, m - 1, dp)

    def __memoUtil(self, i, j, dp):
        if i < 0 or j < 0:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]

        if self.A[i] is self.B[j]:
            dp[i][j] = 1 + self.__memoUtil(i - 1, j - 1, dp)
        else:
            dp[i][j] = max(
                self.__memoUtil(i, j - 1, dp), self.__memoUtil(i - 1, j, dp)
            )

        return dp[i][j]
    
    def tabulation(self):
        n = len(self.A)
        m = len(self.B)

        dp = [[-1 for j in range(m+1)] for i in range(n+1)]

        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if self.A[i - 1] == self.B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j], dp[i][j - 1]
                    )
        
        self.dp = dp
        return dp[n][m]

    def print_lcs(self):
        m = len(self.A)
        n = len(self.B)

        i, j = m, n

        dp = self.dp
        matched = ['$' for _ in range(dp[m][n])]
        idx = dp[m][n] - 1

        while i > 0 and j > 0:
            if self.A[i - 1] == self.B[j - 1]:
                matched[idx] = self.A[i - 1] 
                idx -= 1
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        # Prints the table
        # for i in range(m + 1):
        #     for j in range(n + 1):
        #         print(self.dp[i][j], end=" ")
        #     print("\n")

        return str("".join(matched))