import gym
import game
#gym.logger.set_level(40)
inkey = game._Getch()
LEFT = 0
RIGHT = 1

arrow_keys = {
    b'd' :RIGHT,
    b'a' :LEFT,
}    

env = gym.make('CartPole-v0')

env.reset()
env.render()
done = False
while done != False:
    key = inkey()
    if key != b'\x00':
        action = arrow_keys[key]
        state, reward, done,_ = env.step(action)
        env.render()
