import gym
import sys

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            try:
                self.impl = _GetchMacCarbon()
            except AttributeError:
                self.impl = _GetchUnix()

    def __call__(self): return self.impl()
class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

inkey = _Getch()
LEFT = 0
DOWN = 1
RIGHT = 2
UP =3

arrow_keys = {
    b'w' : UP,
    b's' :DOWN,
    b'd' :RIGHT,
    b'a' :LEFT,
}    


if __name__ =="__main__":
    
    from gym.envs.registration import register

    register(
        id = 'FrozenLake-v1',
        entry_point = 'gym.envs.toy_text:FrozenLakeEnv',
        kwargs = {'map_name' : '4x4', 'is_slippery' :True}
    )
    env = gym.make('FrozenLake-v1')
    env.render(mode='human')
    while True:
        key = inkey()
        print(key)
        if key not in arrow_keys.keys() and key !=b'\x00':
            print("you pressed",key)
            print("Game aborted!")
            break
        if key != b'\x00':
            action = arrow_keys[key]
            state, reward, done ,info = env.step(action)
            env.render(mode='human')
            print("State : ",state, "action : ", action, "reward : ", reward,"info : ", info)
            if done:
                print("Finished with reward" ,reward)
                break

