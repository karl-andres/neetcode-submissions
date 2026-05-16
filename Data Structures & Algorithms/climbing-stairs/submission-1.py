class Solution:
    def climbStairs(self, n: int) -> int:
        # base cases
        if n <= 2:
            return n
        
        second_last = 1
        last = 2
        curr_stair = second_last + last
        
        # iteration, bottom up (tabulation)
        for i in range(3, n + 1):
            curr_stair = second_last + last
            second_last = last
            last = curr_stair

        return curr_stair