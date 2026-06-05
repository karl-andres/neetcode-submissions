class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)

        for i in range(len(strs)):
            freq_count = [0] * 26
            word = strs[i]
            for c in word:
                index = ord(c) - 97
                freq_count[index] += 1
            freq_map[tuple(freq_count)].append(word)
        
        return list(freq_map.values())