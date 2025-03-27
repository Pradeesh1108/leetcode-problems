class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_w = float("-inf")

        while l < r:
            mi = min(height[l], height[r])
            width = r - l

            if height[l] < height[r]:
                l +=1
            else:
                r-=1
            max_w = max(max_w, mi*width)

        return max_w

        
