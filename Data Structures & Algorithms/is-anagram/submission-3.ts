class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const frequency_s = new Map<string, number>();
        const frequency_t = new Map<string, number>();
        
        // count frequnecy for s
        for (let i = 0; i < s.length; i++) {
            frequency_s.set(s[i], (frequency_s.get(s[i]) ?? 0) + 1);
        }

        // count frequnecy for t
        for (let i = 0; i < t.length; i++) {
            frequency_t.set(t[i], (frequency_t.get(t[i]) ?? 0) + 1);
        }
        
        if (frequency_s.size === frequency_t.size) {
            for (const [char, count] of frequency_s) {
                if (frequency_t.get(char) !== count) {
                    return false;
                }
            }
        } else {
            return false
        }
        return true
    }
}
