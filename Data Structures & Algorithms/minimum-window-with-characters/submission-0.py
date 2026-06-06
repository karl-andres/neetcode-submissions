class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if s and t are empty, or t is longer than s. it's impossible
        if not s or not t or len(t) > len(s):
            return ""

        # frequency array for string t
        freq_t = [0] * 128

        # frequency array foor string s keeping track of required chars and their freqs
        freq_s = [0] * 128

        for c in t:
            index = ord(c)
            freq_t[index] += 1

        required = 0
        for count in freq_t:
            if count > 0:
                required += 1

        l = 0 
        best_len = float('inf')
        best_l = 0
        formed = 0

        result = ""

        for r in range(len(s)):
            char = s[r]
            curr_idx = ord(char)
            freq_s[curr_idx] += 1

            if freq_t[curr_idx] > 0 and freq_s[curr_idx] == freq_t[curr_idx]:
                formed += 1
            
            while formed == required:
                curr_len = r - l + 1

                if curr_len < best_len:
                    best_len = curr_len
                    result = s[l:r + 1]

                # check l pointer char and decrement
                l_index = ord(s[l])
                freq_s[l_index] -= 1

                # check if formed still satisfies
                if freq_t[l_index] > 0 and freq_s[l_index] < freq_t[l_index]:
                    formed -= 1
                
                l += 1
            
        if best_len == float('inf'):
            return ""

        return result