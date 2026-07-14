class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i<j:
            m = (j+i)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                i=m+1
            else:
                j=m-1
        if nums[i] == target:
            return i
        else:
            return -1