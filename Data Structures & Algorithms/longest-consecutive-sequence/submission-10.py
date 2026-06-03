"""
{2,20,4,10,3,4,5}

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        convert = set(nums)
        res = 0
        for n in nums:
            if (n - 1) in nums:
                continue

            counter = 1
            while (n + counter) in nums:
                counter += 1
            
            res = max(res, counter)
        return res