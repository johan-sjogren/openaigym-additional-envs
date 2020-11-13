from gym.envs.registration import register

register(
    id='SimpleContMountainCar-v0',
    entry_point='gym_simplecontmountaincar.envs:SimpleMountainCar',
    max_episode_steps=999,
    reward_threshold=90.0,
)