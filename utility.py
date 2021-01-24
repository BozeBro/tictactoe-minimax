def iswinner(board, piece: str) -> int:
    """
    piece - string - Either an "X" or "O"
    Checks if win conditions are met.
    Could check only relevant squares but not as readable.
    """
    # Checks each row, then each col, and then the diagonals
    for line in [[x + 3 * y for x in range(3)] for y in range(3)] + \
    [[3 * x + y for x in range(3)] for y in range(3)] + \
    [[3 * x + x for x in range(3)]] + \
    [[3 * x + 2 - x for x in range(3)]]:
        if all(board[sq] == piece for sq in line):
            return True
    return False

def isvalid(sq: int, board) -> bool:
    if 0 <= sq < 9 and board[sq] not in {"X", "O"}:
        return True
    return False
def print_board(board):
    """Format the board on console so it looks nice"""
    for i, sq in enumerate(board):
        end = 1 if not (i + 1) % 3 else 0
        print(sq + " | " * (not end), end="\n" * end)
        # Do not print line after final row
        if end and i+1 != 9:
            print("---" * 3)
    print()
