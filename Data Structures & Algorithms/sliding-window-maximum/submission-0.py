import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r = k - 1
        res = []
        for l in range(len(nums) - k + 1):
            sub_array = nums[l:r + 1]
            sub_array_max_heap = [-x for x in sub_array]
            heapq.heapify(sub_array_max_heap)
            max_val = -1 * sub_array_max_heap[0]
            res.append(max_val)
            r += 1
        
        return res