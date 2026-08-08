class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        if len(coins) == 0:
            return 0

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return dp[amount] if dp[amount] != amount + 1 else -1

        
    def coinChange_td(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        n = len(coins)

        if n == 0:
            return 0

        memo = {}

        def dfs(amount):

            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

