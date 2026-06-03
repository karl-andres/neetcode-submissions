class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += str(len(word)) + "#" + word
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        cnt = 0
        while cnt < len(s):
            num = ""
            while s[cnt].isdigit():
                num += s[cnt]
                cnt += 1
            cnt += 1
            word = ""
            for i in range(int(num)):
                word += s[cnt]
                cnt += 1
            res.append(word)

        return res