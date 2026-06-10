class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const seen = new Set<number>();

        for (let i = 0; i < nums.length; i++) {
            if (seen.has(nums[i])) {
                return true
            }
            seen.add(nums[i])
        }
        return false
    }
}
