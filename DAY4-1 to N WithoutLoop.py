def printNos(x: int) -> List[int]: 

    if x == 0:

        return []

    else:

        arr = printNos(x-1)

        arr.append(x)

        return arr



https://www.codingninjas.com/studio/problems/1-to-n-without-loop_9065112?challengeSlug=ninja-slayground
