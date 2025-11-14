from src.behavior_tree import build_behavior_tree
from src.world.environment import PacMan, Environment

env = Environment()
pacman = PacMan(env)
tree = build_behavior_tree(pacman)

# Simulação de passos do jogo
for step in range(10):
    print(f"\n--- Passo {step + 1} ---")
    tree.run()
