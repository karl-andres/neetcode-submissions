import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(nums)
        length = len(nums)

        for i in range(length - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)