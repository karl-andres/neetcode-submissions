class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        bucket = [[] for i in range(len(nums) + 1)]
        
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        for num, cnt in freq.items():
            bucket[cnt].append(num)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            while bucket[i] != []:
                res.append(bucket[i].pop())
                if len(res) == k:
                    return res