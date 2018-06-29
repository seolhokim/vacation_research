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
key =""
while key != 'q':
    key = inkey()
    print(key)
