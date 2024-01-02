class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        is_in=False
        for i in reversed(word):
            for row in board:
                if i in row:
                    is_in=True
            if not is_in:
                return False
        recent_places=[]
        def solve_problem(letter_no, row, col):
            if letter_no == len(word) and word[letter_no-1]==word[-1]:
                return True

            for i in ((1, 0), (-1, 0), (0, 1), (0, -1)):

                if 0 <= row + i[0] < len(board) and 0 <= col + i[1] < len(board[0]) and not (row+i[0],col+i[1]) in recent_places:

                    if board[row + i[0]][col + i[1]] == word[letter_no]:
                        recent_places.append((row,col))
                        if solve_problem(letter_no + 1, row + i[0], col + i[1]):
                            return True
                        else:
                            recent_places.pop()
            return False


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    recent_places=[]
                    if solve_problem(1, row, col):
                        return True
                    
                        
        return False