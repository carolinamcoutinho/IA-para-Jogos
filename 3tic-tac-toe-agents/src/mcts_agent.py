from game import Game, PLAYER_X, PLAYER_O
import random, math, time

class MCTSNode:
    def __init__(self, game: Game, player_to_move, parent=None, move=None):
        self.game = game
        self.parent = parent
        self.move = move
        self.player_to_move = player_to_move
        self.children = []
        self.visits = 0
        self.wins = 0.0

    def is_fully_expanded(self):
        return len(self.children) == len(self.game.available_moves())

    def expand(self):
        tried = {c.move for c in self.children}
        for m in self.game.available_moves():
            if m not in tried:
                g = self.game.copy()
                g.make_move(m, self.player_to_move)
                next_player = PLAYER_O if self.player_to_move==PLAYER_X else PLAYER_X
                child = MCTSNode(g, next_player, parent=self, move=m)
                self.children.append(child)
                return child
        return None

    def best_child(self, c_param=1.4):
        choices = []
        for child in self.children:
            if child.visits == 0:
                return child
            uct = (child.wins/child.visits) + c_param*math.sqrt(math.log(self.visits)/child.visits)
            choices.append((uct, child))
        return max(choices, key=lambda x: x[0])[1]

def default_policy(game: Game, player_to_move):
    g = game.copy()
    current = player_to_move
    while not g.is_terminal():
        m = random.choice(g.available_moves())
        g.make_move(m, current)
        current = PLAYER_O if current==PLAYER_X else PLAYER_X
    return g.winner()

class MCTSAgent:
    def __init__(self, player=PLAYER_O, time_limit=0.2):
        self.player = player
        self.time_limit = time_limit

    def select_move(self, game: Game):
        root = MCTSNode(game.copy(), self.player)
        end_time = time.time() + self.time_limit
        while time.time() < end_time:
            node = root
            # selection
            while node.children and node.is_fully_expanded():
                node = node.best_child()
            # expansion
            if not node.game.is_terminal():
                node = node.expand() or node
            # simulation
            winner = default_policy(node.game, node.player_to_move)
            # backprop
            self.backpropagate(node, winner)
        best = max(root.children, key=lambda c: c.visits) if root.children else None
        return best.move if best else random.choice(game.available_moves())

    def backpropagate(self, node, winner):
        while node:
            node.visits += 1
            if winner == self.player:
                node.wins += 1
            elif winner == "DRAW":
                node.wins += 0.5
            node = node.parent
