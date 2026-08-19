class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        need = [amount + 1] * (amount + 1)
        need[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    need[i] = min(need[i], 1 + need[i - coin])

        return need[amount] if need[amount] != amount + 1 else -1