def findDuplicate(arr):

    d= {}

    for i in arr:

        if i in d:

            return i

        else:

            d[i] = 1 
