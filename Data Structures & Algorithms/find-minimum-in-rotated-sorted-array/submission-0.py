class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1]:
            return nums[0]
        n = len(nums)
        i = 0
        j = n-1
        while i < j:
            # print(i, j)
            m = (i+j)//2
            if j - i == 1:
                return min(nums[i], nums[j])
            if nums[m] > nums[i]:
                i = m
            else:
                j = m
        return nums[i]
            
                