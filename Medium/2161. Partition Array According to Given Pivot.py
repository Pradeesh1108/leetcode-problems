class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        leftArr = []
        rightArr = []
        count = 0

        for i in range(n):
            if nums[i] == pivot:
                count+=1
            elif nums[i] > pivot:
                rightArr.append(nums[i])
            else:
                leftArr.append(nums[i])

        return leftArr + [pivot] * count + rightArr
        
