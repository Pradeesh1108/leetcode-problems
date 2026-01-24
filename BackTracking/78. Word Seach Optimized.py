from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        board_count = Counter(c for row in board for c in row)
        word_count = Counter(word)

        for c in word_count:
            if word_count[c] > board_count.get(c, 0):
                return False

        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

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