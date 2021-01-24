import itertools, random
from functools import partial
from utility import iswinner, isvalid, print_board
from minimax import *
def user_move(board, *_) -> int:
    """Game Logic for user"""
    while True:
        try:
            sq =  int(input("Make a move on the board: "))
            if isvalid(sq, board):
                return sq
            print("Not a valid square")
        except ValueError:
            print("NOT a number")
def game(p1: str, p2: str, move, board):
    """
    p1 - string - Can be a bot or a user.
    p2 - string - Always a bot.
    move - dict[string] - contains info on how a player will move
    Implements the tic-tac-toe game.
    """
    board = [str(x) for x in range(9)]
    player = itertools.cycle((p1, p2))
    piece = itertools.cycle(("X", "O"))
    # Default message if outcome is a draw.
    winner = "No one"
    print(f"It is {p1}'s turn", end="\n\n")
    print_board(board)
    counter = 0
    while (counter:=counter+1) <= 9:
        cur_play, cur_piece = next(player), next(piece)
        sq = move[cur_play](board, counter - 1, cur_piece)
        board[sq] = cur_piece
        print(f"It is {cur_play}'s turn")
        print_board(board)
        if iswinner(board, cur_piece):
            winner = cur_play
            break
    print(f"{winner} is the winner!")
def random_move(board, *_):
    while True:
        sq = random.randint(0, 8)
        if isvalid(sq, board):
            return sq
bot = partial(minimax, maximizing=True, square=None)
def bot_move(board, count, piece):
    _, sq = bot(board, count=count, piece=piece)
    return sq
board = [str(x) for x in range(9)]
move = {"user": user_move, "bot": bot_move, "rand": random_move}
game("user", "bot", move, board)