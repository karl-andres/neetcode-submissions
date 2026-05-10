class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, nums in enumerate(nums):
            complement = target - nums
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums] = i
        return False