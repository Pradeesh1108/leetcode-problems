class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        string = ""
        idx = 0
        
        for i, char in enumerate(s):
            if idx < len(spaces) and i == spaces[idx]:
                string += " "
                idx += 1
            string+= char

        return string

        
