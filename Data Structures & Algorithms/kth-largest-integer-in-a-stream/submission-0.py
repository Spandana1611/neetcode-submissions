import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)


    def add(self, val: int) -> int:
        i = bisect.bisect_right(self.nums, val)
        self.nums = self.nums[:i] + [val] + self.nums[i:]
        return self.nums[-1*self.k]
