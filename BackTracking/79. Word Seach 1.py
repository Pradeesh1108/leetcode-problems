class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backTrack(x,y,index):

            if index == len(word):
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[index]:
                return False

            t = board[x][y]
            board[x][y] = "."

            found = (
                backTrack(x+1, y, index + 1) or
                backTrack(x-1, y, index + 1) or
                backTrack(x, y+1, index + 1) or
                backTrack(x, y-1, index + 1)
                
            )

            board[x][y] = t

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backTrack(i, j, 0):
                        return True

        return False