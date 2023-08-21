from os import *
from sys import *
from collections import *
from math import *
n=int(input())
l=[int(x) for x in str(n)]
sum=0
for i in l:
    sum+=(i**len(l))
if sum==n:
    print("true")
else:
    print("false")


https://www.codingninjas.com/studio/problems/check-armstrong_9065114?challengeSlug=ninja-slayground
