class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n < 2:
            return 0

        l,r = 0,1
        maxp = 0
        while r < n:
            if prices[l] > prices[r]:
                l = r
            else:
                maxp = max(maxp, prices[r] - prices[l])
            r += 1

        return maxp
                
        