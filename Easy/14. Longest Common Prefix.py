class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return ""
        min_str = min(strs,key=len)
        for i, char in enumerate(min_str):
            for other_str in strs:
                if other_str[i] != char:
                    return min_str[:i]
        return min_str
        
