class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i-index))
                start = index
            stack.append((start,h))
            
        while stack:
            i, hight = stack.pop()
            max_area = max(max_area, hight * (len(heights)-i))
        return max_area
                
