import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # pop both
            stone_x = heapq.heappop_max(stones)
            stone_y = heapq.heappop_max(stones)

            # reverse order bc using heapmax api
            if stone_x  > stone_y:
                new_y = stone_x - stone_y
                heapq.heappush_max(stones, new_y)
            
        return stones[0] if stones else 0