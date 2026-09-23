"""
226
[0,0,1,1]

"""

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i + 1]
            if (i <= len(s) - 2) and (10 <= int(s[i:i + 2]) <= 26):
                dp[i] += dp[i + 2]
        
        return dp[0]