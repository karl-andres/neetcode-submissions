class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                temp_profit = prices[j] - prices[i]
                if temp_profit > max_profit:
                    max_profit = temp_profit
        return max_profit