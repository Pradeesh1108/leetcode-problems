class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        sums = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
                n = dic[s[i+1]] -dic[s[i]]
                sums+=n
                i+=2
            else:
                sums+=dic[s[i]]
                i+=1

        return sums
