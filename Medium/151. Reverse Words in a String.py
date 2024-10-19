class Solution:
    def reverseWords(self, s: str) -> str:
        words = [word for word in s.split(" ") if word]
        rw = words[::-1]
        rs = ' '.join(rw)
        return rs
         
