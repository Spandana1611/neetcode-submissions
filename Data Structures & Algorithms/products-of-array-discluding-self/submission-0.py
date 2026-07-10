class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pl = []
        for i in nums:
            if len(pl) == 0:
                pl.append(i)
            else: pl.append(i*pl[-1])
        pr = []
        for i in range(len(nums)-1,-1,-1):
            if len(pr) == 0:
                pr.append(nums[i])
            else: pr.append(nums[i]*pr[-1])
        ans = []
        for i in range(len(nums)):
            if i==0:
                ans.append(pr[-2])
            elif i==len(nums)-1:
                ans.append(pl[-2])
            else:
                ans.append(pl[i-1]*pr[-2-i])
        return ans