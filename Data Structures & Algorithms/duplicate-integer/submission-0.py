class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        u = list(set(nums))
        return len(u) != len(nums)
            