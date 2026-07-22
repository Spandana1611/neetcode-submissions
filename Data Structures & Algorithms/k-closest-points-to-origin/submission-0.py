class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [[points[i][0]**2+points[i][1]**2, i] for i in range(len(points))]
        heapq.heapify(min_heap)
        ans = []
        i=0
        while i<k:
            point = heapq.heappop(min_heap)
            ans.append(points[point[1]])
            i+=1

        return ans