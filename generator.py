"""The generator file should accomplish the following task
    1. generate random number when calling a function
"""
import random 

def gen_rand():
    return random.randint(0,2**32)