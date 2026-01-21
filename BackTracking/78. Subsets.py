class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def backTrack(i):
            if i >= len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[i])
            backTrack(i+1)

            
            subset.pop()
            backTrack(i+1)

        backTrack(0)

        return result