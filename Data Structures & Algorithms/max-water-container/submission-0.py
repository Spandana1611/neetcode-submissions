class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = min(heights[0], heights[1])
        n = len(heights)
        for i in range(n-1):
            for j in range(i+1,n):
                ans = max(ans, (j-i)*min(heights[i], heights[j]))
        return ans