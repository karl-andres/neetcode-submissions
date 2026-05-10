class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        sorted_s1 = sorted(s1)
        l = 0
        for r in range(len(s1) - 1, len(s2)):
            sub = s2[l:r+1]
            sorted_sub = sorted(sub)
            if sorted_s1 == sorted_sub:
                return True
            l += 1
        return False