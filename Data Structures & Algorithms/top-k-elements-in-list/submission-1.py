class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        ans = []
        for i in nums:
            d[i] += 1
        a = [[d[i], i] for i in d.keys()]
        a.sort(reverse=True)
        for i in range(k):
            ans.append(a[i][1])
        return ans