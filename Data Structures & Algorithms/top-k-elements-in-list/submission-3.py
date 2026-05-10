class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        
        arr = []

        for num, cnt in freq.items():
            arr.append([cnt, num])
        

        arr.sort()
        print(arr)
        res = []
        for i in range(len(arr) - 1, -1, -1):
            value = arr[i][1]
            res.append(value)
            if len(res) == k:
                return res
