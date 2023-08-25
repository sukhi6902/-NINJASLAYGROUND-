from collections import *

from math import *
def fahrenheitToCelsius(s, e, w):

    a=[]

    for i in range(s,e+1,w):

        x=int((i-32)*5/9)

        s=i

        a.append((s,x))

    return a
