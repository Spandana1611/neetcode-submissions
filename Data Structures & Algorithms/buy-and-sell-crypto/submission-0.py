class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(n-1):
            for j in range(i+1,n):
                ans = max(prices[j]-prices[i], ans)
        return ans