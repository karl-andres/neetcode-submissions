class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = [c for c in s if c.isalnum()]

        temp2 = "".join(temp)
        alpha_num = temp2.lower()

        l = 0
        r = len(alpha_num) - 1
        while l < r:
            if alpha_num[l] != alpha_num[r]:
                return False
            l += 1
            r -= 1
        return True