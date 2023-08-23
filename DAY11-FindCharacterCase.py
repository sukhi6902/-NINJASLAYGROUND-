from os import *
from sys import *
from collections import *
from math import *

def numberPattern(n):
    a = 1
    b = []
    for i in range(n - 1, -1, -1):
        c = []
        for j in range(n):
            if j < i:
                c.append(-1)
            else:
                c.append(a)
                a += 1
                if a == 10:
                    a = 1
        b.append(c)
    return b


https://www.codingninjas.com/studio/problems/crazy-numbers_9065119?challengeSlug=ninja-slayground&leftPanelTab=1
