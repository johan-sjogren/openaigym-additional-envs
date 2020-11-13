from gym.envs.registration import register

register(
    id='SimpleContMountainCar-v0',
    entry_point='gym_simplecontmountaincar.envs:SimpleMountainCar',
)