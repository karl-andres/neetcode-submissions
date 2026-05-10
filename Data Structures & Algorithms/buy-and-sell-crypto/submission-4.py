class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l, r = 0, 1
        profit = 0
        while l < r:
            if prices[l] < prices[r]:
                current_prof = prices[r] - prices[l]
                profit = max(profit, current_prof)
                r += 1
            elif prices[l] > prices[r]:
                l = r
                r += 1
            else: 
                r += 1
            if ((len(prices)) == r):
                break
        return profit