# usr/bin/python
__author__ = 'aadit'
import random

replies = {'hi' : ['Hello','How are you?', 'Glad to hear from you!'],'':['None']}

def exists(message):
    """
        exists(key_to_be_matched) -> bool
        return True if message in replies
    """
    message = message.split()
    for m in message:
        if m in replies.keys():
            return m
            break
        else:
            return None
            continue


def generate(matched_key):
    """
        generate(matched_key) -> list
        return the available replies of the corresponding key
    """

    reply = replies.get(matched_key)
    return reply

def get_reply(list):
    """
        get_reply(list) -> str
        return a random index and show a random reply
    """


    index = random.randint(0,len(list)-1)
    return list[index]
