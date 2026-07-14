import math

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if n==1:
            return 1
        p_idx = [[position[i], i, (target-position[i])/speed[i]] for i in range(n)]
        p_idx.sort(reverse=True)
        # print(p_idx)
        i = 1
        ans = 0
        while i<n:
            x = i
            if p_idx[i][2] > p_idx[i-1][2]:
                if i<n-1 and p_idx[i][2] >= p_idx[i+1][2]:
                    i+=1
                else:
                    i+=1
                    ans+=1
                if x==1: ans+=1
                continue
            while i<n and p_idx[i][2] <= p_idx[x-1][2]:
                i+=1
            ans+=1
        return ans