import numpy as np
import gymnasium as gym
import random

class QLearningAgent:
    def __init__(self, env_name, alpha=0.8, gamma=0.95, epsilon=1.0,
                 epsilon_min=0.01, epsilon_decay=0.995, episodes=5000, **env_kwargs):
        
        self.env = gym.make(env_name, **env_kwargs)
        self.env_name = env_name
        self.alpha = alpha
        self.gamma = gamma

        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        
        self.episodes = episodes

        self.q_table = np.zeros((self.env.observation_space.n,
                                 self.env.action_space.n))

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return self.env.action_space.sample()
        return int(np.argmax(self.q_table[state]))

    def train(self):
        rewards = []
        for ep in range(self.episodes):
            state, _ = self.env.reset()
            total_reward = 0
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, terminated, truncated, _ = self.env.step(action)
                done = terminated or truncated

                best_next = np.max(self.q_table[next_state])

                # Q-learning update
                self.q_table[state, action] += self.alpha * (
                    reward + self.gamma * best_next - self.q_table[state, action]
                )

                state = next_state
                total_reward += reward

            rewards.append(total_reward)
            self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)

            if (ep + 1) % 500 == 0:
                print(f"{self.env_name} | Episódio {ep+1}/{self.episodes} | ε={self.epsilon:.4f}")

        return rewards
