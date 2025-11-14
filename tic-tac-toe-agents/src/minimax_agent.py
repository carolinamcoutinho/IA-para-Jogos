# src/minimax_agent.py
from game import Game, PLAYER_X, PLAYER_O, EMPTY
import math

class MinimaxAgent:
    def __init__(self, player=PLAYER_X, max_depth=9):
        self.player = player
        self.opp = PLAYER_O if player==PLAYER_X else PLAYER_X
        self.max_depth = max_depth

    def evaluate(self, game: Game):
        win = game.winner()
        if win == self.player:
            return 1
        elif win == self.opp:
            return -1
        elif win == "DRAW":
            return 0
        return None  # non-terminal

    def minimax(self, game: Game, depth, alpha, beta, maximizing):
        eval_term = self.evaluate(game)
        if eval_term is not None or depth==0:
            return eval_term if eval_term is not None else 0

        if maximizing:
            max_eval = -math.inf
            for m in game.available_moves():
                g = game.copy()
                g.make_move(m, self.player)
                val = self.minimax(g, depth-1, alpha, beta, False)
                max_eval = max(max_eval, val)
                alpha = max(alpha, val)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for m in game.available_moves():
                g = game.copy()
                g.make_move(m, self.opp)
                val = self.minimax(g, depth-1, alpha, beta, True)
                min_eval = min(min_eval, val)
                beta = min(beta, val)
                if beta <= alpha:
                    break
            return min_eval

    def select_move(self, game: Game):
        best_score = -math.inf
        best_move = None
        for m in game.available_moves():
            g = game.copy()
            g.make_move(m, self.player)
            score = self.minimax(g, self.max_depth-1, -math.inf, math.inf, False)
            if score > best_score:
                best_score = score
                best_move = m
        return best_move
