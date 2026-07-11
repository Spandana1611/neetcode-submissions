class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=1
        ans=0
        present = 0

        while j<n:
            if height[j] < height[i]:
                present += (height[i] - height[j])
                j+=1
            else:
                ans+=present
                present = 0
                i = j 
                j+=1
            if j == n:
                height[i] -= 1
                j=i+1
                present = 0
        return ans
