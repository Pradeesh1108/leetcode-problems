class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set1 = set(nums)
        nums.clear()
        for i in set1:
            nums.append(i)
        nums.sort()
        return len(nums)
