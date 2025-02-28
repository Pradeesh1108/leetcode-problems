class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]

        for i in nums:
            count[i] +=1
        
        red, white, blue = count

        nums[:red] = [0] * red
        nums[red:red+white] = [1] * white
        nums[red+white:] = [2] * blue
