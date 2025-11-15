from game import Game, PLAYER_X, PLAYER_O
from minimax_agent import MinimaxAgent
from mcts_agent import MCTSAgent
from random_agent import RandomAgent

def play_game(agent_x, agent_o, verbose=True):
    g = Game()
    current = PLAYER_X
    while not g.is_terminal():
        if verbose:
            print("\nBoard 1:")
            g.print_board()
        if current == agent_x.player:
            move = agent_x.select_move(g)
        else:
            move = agent_o.select_move(g)
        if verbose:
            print(f"\n{current} plays at {move}")
        g.make_move(move, current)
        current = PLAYER_O if current==PLAYER_X else PLAYER_X
    if verbose:
        print("\nFinal Board:")
        g.print_board()
        print("Result:", g.winner())
    return g.winner()

if __name__ == "__main__":
    x_agent = MinimaxAgent(player=PLAYER_X)
    o_agent = MCTSAgent(player=PLAYER_O, time_limit=0.05)
    play_game(x_agent, o_agent, verbose=True)
