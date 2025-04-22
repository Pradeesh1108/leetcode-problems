"""
sol 1
"""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        min_max = 0
        for i in range(n//2):
            min_max = max(min_max, nums[i] + nums[n-1-i])
        return min_max


"""
sol 2
"""

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []

        l,r = 0, len(nums) - 1

        while l<r:
            pairs.append(nums[l] + nums[r])
            l+=1
            r-=1
        return max(pairs)

        
