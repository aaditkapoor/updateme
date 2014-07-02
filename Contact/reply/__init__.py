__author__ = 'aadit'

VERSION = ('1..0.0.0','Final','Release')

def get_version(*args):
    for i in args:
        if i == 'reply':
            return 'Reply version: 1.0.0.0'

    return VERSION