class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_rec = 0
        n_cols = len(matrix[0])
        heights = [0] * (n_cols)
        
        for row in matrix:
            for i in range(n_cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            print(heights)

            stack = []
            # for i in range(n_cols):
            #     while stack and heights[i] < heights[stack[-1]]:
            #         h = heights[stack.pop()]
            #         w = i if not stack else i - stack[-1] - 1
            #         max_rec = max(max_rec, h * w)
            #     stack.append(i)

            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    max_rec = max(max_rec, height * (i-index))
                    start = index
                stack.append((start,h))
                
            while stack:
                i, hight = stack.pop()
                max_rec = max(max_rec, hight * (len(heights)-i))
                
        return max_rec
