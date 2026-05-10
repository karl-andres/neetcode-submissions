class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp = nums1 + nums2
        temp.sort()
        combined = temp
        
        totalLen = len(combined)

        if totalLen % 2 == 0:
            return (combined[totalLen // 2] + combined[(totalLen // 2) - 1]) / 2
        else:
            return combined[totalLen // 2]

