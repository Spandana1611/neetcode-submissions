class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = [[nums[i], i] for i in range(len(nums))]
        nums_idx.sort()
        i = 0
        j = len(nums_idx)-1
        while i<j:
            if nums_idx[i][0] + nums_idx[j][0] == target:
                return [min(nums_idx[i][1], nums_idx[j][1]), max(nums_idx[i][1], nums_idx[j][1])]
            if nums_idx[i][0] + nums_idx[j][0] < target:
                i+=1
            else:
                j-=1
        return [min(nums_idx[i][1], nums_idx[j][1]), max(nums_idx[i][1], nums_idx[j][1])]
            