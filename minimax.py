from utility import iswinner, isvalid, print_board
"""
Not handling depth for this simple minimax implementation.
"""
def minimax(board, piece, maximizing, count, square):
    next_piece = "X" if piece == "O" else "O"
    if count == 9:
        return 0, square
    elif maximizing:
        val = -float("infinity")
        for sq in range(9):
            if isvalid(sq, board):
                board[sq] = piece
                if iswinner(board, piece):
                    board[sq] = str(sq)
                    # Running this code on the next person's turn
                    return 1, sq
                max_val, _ = minimax(board, next_piece, not maximizing, count+1, square)
                if max_val > val:
                    square = sq
                val = max(val, max_val)
                board[sq] = str(sq)
        return val, square
    else:
        val = float("infinity")
        for sq in range(9):
            if isvalid(sq, board):
                board[sq] = piece
                if iswinner(board, piece):
                    board[sq] = str(sq)
                    return -1, sq
                min_val, _ = minimax(board, next_piece, not maximizing, count+1, square)
                if min_val < val:
                    square = sq
                val = min(val, min_val)
                board[sq] = str(sq)
        return val, square
