# src/random_agent.py
import random
class RandomAgent:
    def __init__(self, player):
        self.player = player
    def select_move(self, game):
        return random.choice(game.available_moves())
