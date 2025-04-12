class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        allowed = set(allowed)
        res = 0
        for i in words:
            if set(i) <= allowed:
                res+=1
        return res
        
