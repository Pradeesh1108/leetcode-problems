class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        arr = []
        def is_prime(n):
            if i<2:
                return False
            if i in (2,3,5):
                return True
            if i%2==0 or i%3==0 or i%5==0:
                return False
            for j in range(7,int(math.sqrt(i))+1,2):
                if i%j==0:
                    return False
            return True

        for i in range(left,right+1):
            if is_prime(i):
                arr.append(i)

        if len(arr)<2:
            return [-1,-1]

        mini = float('inf')

        arr2 = [0,0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < mini:
                arr2[0] = arr[i]
                arr2[1] = arr[i+1]
                mini = arr[i+1] - arr[i]

        return arr2
                    
