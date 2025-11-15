from qlearning_agent import QLearningAgent
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    agent = QLearningAgent(
        env_name="FrozenLake-v1",
        is_slippery=True,      # você pode usar False para facilitar o aprendizado
        episodes=3000,
        alpha=0.8,
        gamma=0.95,
        epsilon_decay=0.998
    )

    rewards = agent.train()

    # gráfico suavizado
    smoothed = np.convolve(rewards, np.ones(100)/100, mode="valid")

    plt.plot(smoothed)
    plt.title("Q-learning - FrozenLake")
    plt.xlabel("Episódios")
    plt.ylabel("Recompensa média")
    plt.show()
