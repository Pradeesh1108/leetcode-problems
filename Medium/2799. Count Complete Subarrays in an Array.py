class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        size = len(set(nums))
        count = 0
        n = len(nums)

        for i in range(n):
            count_set = set()
            for j in range(i,n):
                count_set.add(nums[j])
                if len(count_set) == size:
                    count+=1

        return count
