import gym
import gym_simplecontmountaincar
env = gym.make('SimpleContMountainCar-v0')
env.reset()
print(env.step(env.action_space.sample()))
env = gym.make('ContCartPole-v0')
env.reset()
print(env.step(env.action_space.sample()))