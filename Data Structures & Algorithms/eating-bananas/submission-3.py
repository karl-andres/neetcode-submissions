# maximum needed eating rate k is max(piles) (the pile with most bananas)
# minimum hours needed to eat is len(piles)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        lowest_k = 1

        last_working_k = -1

        while lowest_k <= max_k:
            k = (lowest_k + max_k) // 2
            time = 0
            for p in piles:
                time += (p + k - 1) // k # round to next highest whole number
            if time > h:
                lowest_k = k + 1
            else:
                max_k = k - 1
                last_working_k = k
        
        return last_working_k