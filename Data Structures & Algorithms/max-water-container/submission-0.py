class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxWater = 0

        while i < j:
            amount = (j - i) * min(heights[i], heights[j])
            if amount > maxWater:
                maxWater = amount

            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -=1
        
        return maxWater