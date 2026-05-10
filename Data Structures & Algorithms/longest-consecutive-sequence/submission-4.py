class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_list = sorted(set(nums))
        ret = 1
        temp = 1
        for i in range(1, len(sorted_list)):
            if sorted_list[i] == sorted_list[i-1] + 1:
                temp += 1
                if temp > ret:
                    ret = temp
            else:
                temp = 1
        return ret
#(2, 3, 4, 5, 10, 20)