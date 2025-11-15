# src/evaluate.py
from game import Game, PLAYER_X, PLAYER_O
from minimax_agent import MinimaxAgent
from mcts_agent import MCTSAgent
from random_agent import RandomAgent
import random

def tournament(agent_a, agent_b, n=200, verbose=False):
    results = {"A":0, "B":0, "DRAW":0}
    for i in range(n):
        # alternate starting player
        if i%2==0:
            winner = play_once(agent_a, agent_b)
            if winner == agent_a.player:
                results["A"] += 1
            elif winner == agent_b.player:
                results["B"] += 1
            else:
                results["DRAW"] += 1
        else:
            winner = play_once(agent_b, agent_a)
            if winner == agent_b.player:
                results["A"] += 1  # note: swap naming for stats consistency
            elif winner == agent_a.player:
                results["B"] += 1
            else:
                results["DRAW"] += 1
        if verbose and (i+1) % (n//5) == 0:
            print(f"{i+1}/{n} played")
    return results

def play_once(agent_x, agent_o):
    # agents are objects with .player and select_move(game)
    from play_gui import play_game
    return play_game(agent_x, agent_o, verbose=False)

if __name__ == "__main__":
    random.seed(0)
    mm = MinimaxAgent(player=PLAYER_X)
    mcts = MCTSAgent(player=PLAYER_O, time_limit=0.05)
    rand = RandomAgent(player=PLAYER_O)
    print("Minimax vs Random")
    print(tournament(mm, rand, n=100))
    print("MCTS vs Random")
    print(tournament(mcts, rand, n=100))
    print("Minimax vs MCTS")
    print(tournament(mm, mcts, n=100))
