class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        results = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    results[i] = max(results[i], 1 + results[j])
        return max(results)

# [3, 2, 1, 1]

# [1, 3, 4, 2]
#  i  j   