from collections import Counter

def countFrequency(n, m, List):
    a=[]

    count=Counter(List)
    for i in range(1,n+1):
        a.append(count[i])
    return a

https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_9065123?challengeSlug=ninja-slayground&leftPanelTab=0
