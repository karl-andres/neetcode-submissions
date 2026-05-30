import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_list = []
        
        for x, y in points:
            distance = x**2 + y**2
            heap_list.append((distance, [x,y]))

        heapq.heapify(heap_list)

        res = []
        
        for _ in range(k):
            res.append(heapq.heappop(heap_list)[1])

        return res