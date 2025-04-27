class fibonacci:
    def recursion(self, n: int):
        """
        Traditional Recursion Approach
        """

        if n <= 1:
            return n

        return self.recursion(n - 2) + self.recursion(n - 1)

    def memo(self, n: int, memo=None):
        """
        Top-Down Approach
        """

        if memo is None:
            memo = {}

        if n in memo:
            return memo.get(n)
        elif n <= 1:
            return n

        memo[n] = self.memo(n - 2, memo) + self.memo(n - 1, memo)
        return memo[n]

    def tabulation(self, n: int):
        """
        Bottom-Up Approach
        """

        if n <= 1:
            return n

        table = [0 for c in range(n+1)]
        table[1] = 1

        for i in range(2, n+1):
            table[i] = table[i - 2] + table[i - 1]

        return table[i]
