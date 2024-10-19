class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        trans = zip(*matrix)
        for i,row in enumerate(trans):
            matrix[i] = reversed(row)
