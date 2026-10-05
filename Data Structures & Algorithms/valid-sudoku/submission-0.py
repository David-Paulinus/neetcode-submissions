class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkrow(index, length):
            digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            row = board[index]

            for i in range(length):
                if row[i] == ".":
                    continue
                if row[i] not in digits:
                    return False
                if row[i] in digits:
                    digits.remove(row[i])

            return True

        def checkcol(index, length):
            digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            col = board[index]

            for i in range(length):
                row = board[i]
                if row[index] == ".":
                    continue
                if row[index] not in digits:
                    return False
                if row[index] in digits: # Check column value
                    digits.remove(row[index])

            return True

        # need to validate all columns, rows and 3x3 squares
        board_size = 9
        square_size = 3

        row_valid = True
        for i in range(board_size):
            row_valid = row_valid and checkrow(i, board_size)

        col_valid = True
        for i in range(board_size):
            col_valid = col_valid and checkcol(i, board_size)

        squares_valid = True
        for i in range(square_size):
            for j in range(square_size):
                digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

                for p in range(i*square_size, (i*square_size)+square_size):
                    for q in range(j*square_size, (j*square_size)+square_size):
                        print(board[p][q])
                        if board[p][q] == ".":
                            continue
                        if board[p][q] not in digits:
                            squares_valid = False
                        if board[p][q] in digits: 
                            digits.remove(board[p][q])

        print(row_valid, col_valid, squares_valid)
        return row_valid and col_valid and squares_valid


                

        