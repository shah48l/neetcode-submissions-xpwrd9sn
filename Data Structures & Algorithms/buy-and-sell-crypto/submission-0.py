class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_prof = 0
        while r<len(prices):
            if prices[l] > prices[r]:
                l+=1
            else:
                profit = prices[r] - prices[l]
                max_prof = max(max_prof,profit)
            r+=1
        return max_prof