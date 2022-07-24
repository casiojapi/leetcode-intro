class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)    # lista de len = amount + 1, con valor inicializado en cada celda a amount + 1 (que es practicamte lo mismo que setearlo a infinity)
        dp[0] = 0 # inicialiazo el 0 en 0 

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+ dp[a-c])

        return dp[amount] if dp[amount] != amount + 1 else -1