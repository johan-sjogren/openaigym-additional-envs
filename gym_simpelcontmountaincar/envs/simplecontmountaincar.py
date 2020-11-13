import gym

class SimpleMountainCar(gym.envs.classic_control.Continuous_MountainCarEnv):
    """ Turning the cartpole env from an episodic task into a continuing one.
        Only need to rewrite the final part of the step function 
    """
    def step(self, action):
        res = super().step(action)
        reward, done, info = res[1:]

        if not done:
            reward = 0.0

        return np.array(self.state), reward, done, info