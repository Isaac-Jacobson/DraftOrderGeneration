import random
import numpy as np

def getOrder(names, excluded):
    while(True):
        tmp = random.sample(names, len(names))
        if tmp[0] not in excluded: break
    return tmp

def printOrder(names, excluded, seed):
    random.seed(seed)
    print("\n\nThe official order is...\n") 
    for i, n in enumerate(getOrder(names, excluded)):
        print(i+1, ")\t", n)

def makeItLookNice(n, arr):
    n += ":\t"
    if len(n) <= 8: n += "\t"
    for i in arr:
        n += str(f'{i:2.2f}').zfill(5) + '%  '
    return n[:-2]

def printSample(names, excluded, n):
    print("Percentage of the time each player got each draft pick in ", n, " samples")
    print("Player\t\t  1st     2nd     3rd     4th     5th     6th     7th     8th     9th     10th")
    out = np.zeros((len(names), len(names)), dtype="float64")
    for i in range(n):
        order = getOrder(names, excluded)
        for j, name in enumerate(order):
            out[names.index(name)][j] += 1
    arr = np.divide(out, (n/100))
    for i, n in enumerate(names):
        print(makeItLookNice(n, arr[i,:]))
    

