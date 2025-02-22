class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) < abs(closest):
                closest = nums[i]

        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
