class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-1*i for i in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            a,b = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if a!=b:
                heapq.heappush(max_heap, -1*abs(a-b))
        if len(max_heap) == 0: return 0
        return -1*max_heap[0]