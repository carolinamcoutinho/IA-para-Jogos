from qlearning_agent import QLearningAgent
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    agent = QLearningAgent(
        env_name="Taxi-v3",
        episodes=5000,
        alpha=0.7,
        gamma=0.9,
        epsilon_decay=0.999
    )

    rewards = agent.train()

    smoothed = np.convolve(rewards, np.ones(200)/200, mode="valid")

    plt.plot(smoothed)
    plt.title("Q-Learning - Taxi-v3")
    plt.xlabel("Episódios")
    plt.ylabel("Recompensa média")
    plt.show()

    print("\nTreinamento concluído!")
    print("Exemplo da Tabela Q:")
    print(agent.q_table[:10])
