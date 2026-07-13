import bisect

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = []
        for i in range(len(nums)-k+1):
            if i==0:
                q = sorted(nums[:k])
            else:
                if nums[i-1] != nums[i+k-1]:
                    x = bisect.bisect_left(q, nums[i-1])
                    y = bisect.bisect_right(q, nums[i+k-1])
                    # print(q, x, y, i)
                    if y == x:
                        q[x] = nums[i+k-1]
                    elif y>x:
                        for j in range(x,y-1):
                            q[j] = q[j+1]
                        q[y-1] = nums[i+k-1]
                    else:
                        for j in range(x, y, -1):
                            q[j] = q[j-1]
                        q[y] = nums[i+k-1]
            # print(q)
            ans.append(q[-1])
        return ans
