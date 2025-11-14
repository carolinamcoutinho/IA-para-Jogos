# src/game.py
from typing import List, Optional

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),  # rows
    (0,3,6),(1,4,7),(2,5,8),  # cols
    (0,4,8),(2,4,6)           # diags
]

class Game:
    def __init__(self, board: Optional[List[str]] = None):
        self.board = board[:] if board else [EMPTY]*9

    def copy(self):
        return Game(self.board)

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v == EMPTY]

    def make_move(self, pos: int, player: str):
        if self.board[pos] != EMPTY:
            raise ValueError("Invalid move")
        self.board[pos] = player

    def winner(self) -> Optional[str]:
        for a,b,c in WIN_LINES:
            if self.board[a] != EMPTY and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        if EMPTY not in self.board:
            return "DRAW"
        return None

    def is_terminal(self):
        return self.winner() is not None

    def print_board(self):
        b = self.board
        for r in range(3):
            print(f" {b[3*r]} | {b[3*r+1]} | {b[3*r+2]} ")
            if r<2: print("---+---+---")
