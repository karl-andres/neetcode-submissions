import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        hq.heapify(nums);
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        hq.heappush(self.nums, val)
        size = len(self.nums)
        while size > self.k:
            hq.heappop(self.nums)
            size -= 1

        return self.nums[0]