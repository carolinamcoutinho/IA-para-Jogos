from qlearning_agent import QLearningAgent
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    agent = QLearningAgent(env_name="FrozenLake-v1", episodes=3000, is_slippery=True,
                           alpha=0.8, gamma=0.95, epsilon_decay=0.995)
    rewards = agent.train()
    # smooth
    window = 100
    sm = np.convolve(rewards, np.ones(window)/window, mode='valid')
    plt.plot(sm)
    plt.title("Q-Learning - FrozenLake (smoothed)")
    plt.xlabel("Episodes")
    plt.ylabel("Avg Reward")
    plt.show()
