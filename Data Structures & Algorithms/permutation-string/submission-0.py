class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                sub = s2[i:j+1]
                sorted_sub = sorted(sub)
                if sorted_s1 == sorted_sub:
                    return True
        return False