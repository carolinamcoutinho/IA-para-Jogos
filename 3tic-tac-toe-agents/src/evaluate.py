from play_gui import play_game
from minimax_agent import MinimaxAgent
from mcts_agent import MCTSAgent
from random_agent import RandomAgent
from game import PLAYER_X, PLAYER_O

def play_once(agent_x, agent_o):
    return play_game(agent_x, agent_o, verbose=False)

def tournament(agent_a, agent_b, n=100):
    results = {"A":0, "B":0, "DRAW":0}
    for i in range(n):
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
                results["A"] += 1
            elif winner == agent_a.player:
                results["B"] += 1
            else:
                results["DRAW"] += 1
    return results

if __name__ == "__main__":
    mm = MinimaxAgent(player=PLAYER_X)
    mcts = MCTSAgent(player=PLAYER_O, time_limit=0.01)
    rand = RandomAgent(player=PLAYER_O)
    print("Minimax vs Random:", tournament(mm, rand, n=50))
    print("MCTS vs Random:", tournament(mcts, rand, n=50))
    print("Minimax vs MCTS:", tournament(mm, mcts, n=50))
