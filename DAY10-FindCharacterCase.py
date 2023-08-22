from os import *
from sys import *
from collections import *
from math import *

def findCase(ch):

    # Write your code here
    # Return an integer denoting the answer
    if ch.islower():
        return 0
    elif ch.isupper():
        return 1
    else:
        return -1
