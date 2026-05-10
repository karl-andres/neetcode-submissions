class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #BUCKET SORT
        
        counter = {}
        #INITIALIZE BUCKET LIST
        freq = [[] for i in range(len(nums) + 1)]
        #Count frequency
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        #RETRIEVE KEY-VALUE PAIRS
        for n, c in counter.items():
            freq[c].append(n)

        res = []

        #APPEND THE MOST FREQ NUMBERS TO RESULT
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res