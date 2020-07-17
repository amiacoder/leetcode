class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        temp_map = {}
        for i in range(0, 9):
            if 'row' + str(i) not in temp_map:
                temp_map['row' + str(i)] = []
            for j in range(0, 9):
                if 'column' + str(j) not in temp_map:
                    temp_map['column' + str(j)] = []
                sub_board = (i / 3) * 3 + j / 3
                if 'board' + str(sub_board) not in temp_map:
                    temp_map['board' + str(sub_board)] = []
                if board[i][j] in temp_map['row' + str(i)] or board[i][j] in temp_map['column' + str(j)] or board[i][j] in temp_map['board' + str(sub_board)]:
                    # print temp_map, i, j, sub_board
                    return False
                else:
                    if board[i][j] != '.':
                        temp_map['board' + str(sub_board)].append(board[i][j])
                        temp_map['row' + str(i)].append(board[i][j])
                        temp_map['column' + str(j)].append(board[i][j])
        return True
