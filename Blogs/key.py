__author__ = 'aadit'
__version__ = '1.0.0'
import random


class Key():
    def __init__(self, mode, chars=3):
        self.mode = mode
        self.chars = chars

    def generate(self):
        if self.mode == 's':
            if self.chars == 1:
                key = random.randint(1, 10)
            elif self.chars == 2:
                key = random.randint(1, 100)
            elif self.chars == 3:
                key = random.randint(1, 1000)
        elif self.mode == 'm':
            if self.chars == 1:
                key = random.randint(1, 10)
                key = chr(key)
            elif self.chars == 2:
                key = random.randint(1, 100)
                key = chr(key)
            elif self.chars == 3:
                key = random.randint(1, 1000)
                if key >= 225:
                    key -= 755
                    key = chr(key)
        return key

    @staticmethod
    def version():
        return 'Version: 1.0.0.0'


