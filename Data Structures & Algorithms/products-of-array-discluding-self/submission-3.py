"""
[1,1,2,8]
[1,6,24,48]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        totalProduct = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == 0:
                zeros += 1
                continue
            totalProduct *= nums[i]
        
        output = [0] * len(nums)

        if zeros > 1:
            return output

        for i in range(len(nums)):
            if nums[i] == 0:
                output[i] = totalProduct
            else:
                if zeros:
                    output[i] = 0
                else:
                    output[i] = (totalProduct // nums[i])

        return output