class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur_idx):
            # if we reach last index append current permutation to res
            if cur_idx == len(nums):
                res.append(nums.copy())
                return

            # go through every element (swap n times, where n is length of subarray)
            for i in range(cur_idx, len(nums)):
                # swap
                nums[cur_idx], nums[i] = nums[i], nums[cur_idx]
                backtrack(cur_idx + 1)
                # swap back to original since we are backtracking
                nums[cur_idx], nums[i] = nums[i], nums[cur_idx]

        backtrack(0)
        return res