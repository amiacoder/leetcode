class Solution:
    def generateMatrix(self, n):
        column_deltas = [1, 0, -1, 0]
        row_deltas = [0, 1, 0, -1]
        result = [[None for _ in range(0, n)] for _ in range(0, n)]
        i = 1
        row = 0
        column = 0
        corner = 0
        while i <= n**2:
            result[row][column] = i
            column_delta = column_deltas[corner%4]
            row_delta = row_deltas[corner%4]
            next_row = row + row_delta
            next_column = column + column_delta
            # print row, column, next_row, next_column
            if (column_delta == 0 and row == n - 1) or (row_delta == 0 and column == n - 1) or result[next_row][next_column] != None:
                corner += 1
                column_delta = column_deltas[corner%4]
                row_delta = row_deltas[corner%4]
                row = row + row_delta
                column = column + column_delta
                # print 'test', row, column
            else:
                row = next_row
                column = next_column
            i += 1
        return result
