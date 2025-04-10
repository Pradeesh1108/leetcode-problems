class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n-2):
            if len(set(s[i:i+3])) == 3:
                res+=1
        return res
