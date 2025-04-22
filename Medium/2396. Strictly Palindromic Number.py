import numpy as np
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        i = 2
        j = n - 2
        flag = True
        for k in range(i,j+1):
            num = np.base_repr(n,base = k)
            if num != num[::-1]:
                flag = False
                break
        return flag

        
        
