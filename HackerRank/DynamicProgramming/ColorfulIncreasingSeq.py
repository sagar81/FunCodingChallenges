# This solution is built on a form of exclusion, inclusion principle and simple
# DP of O(n^2) which is not good for large arrays. After doing some online research I found that 
# there is an advanced data structure BIT (Binary Indexed Tree) that can be used to reduce O(n^2) to O(nlogn).
# Union and Intersection are not in strict sense the way they are defined in set theory. But making a simple
# venn diagram for 3 colors will help anyone understand what the code is tryign to do.

import sys
import itertools
import math

def getColoredIncreasingSeq(N, K, HC):
    colors = [i for i in range(1, K+1)]
    Union, Intersection = {}, {}

    for r in range(1, K+1):
        for subset in itertools.combinations(colors, r):
            val = getNumberOfIncreasingSeq(list(subset), HC)
            Union[subset] = val
            UpdateIntersection(subset, Union, Intersection)
    return Intersection[subset]

def UpdateIntersection(subset, Union, Intersection):
    if len(subset) == 1:
        Intersection[subset] = Union[subset]
        return
    l = len(subset)
    s = 0
    
    for r in range(1, l):
        for sub in itertools.combinations(list(subset), r):
            s += Intersection[sub]
    Intersection[subset] = Union[subset] - s   

def getNumberOfIncreasingSeq(subset, HC):
    f = {}
    indices = []
    for i in range(len(HC)):
        if HC[i][1] not in subset:
            continue
        f[i] = 1
        indices.append(i)
        l = len(indices)
        for j in range(0, l-1):
            if HC[indices[j]][0] < HC[i][0]:
                f[i] += f[indices[j]]
        f[i] = f[i] % (int(1e9+7))
        
    ret = 0
    for key in f:
        ret += f[key]
    
    return ret % (int(1e9+7))


k = 0
N, K = 0, 0
HC = []

if __name__ == "__main__":
    for line in sys.stdin:
        if  k == 0:
            line = line.rstrip()
            ss = line.split(" ")
            N, K = int(ss[0]), int(ss[1])
        else:
            line = line.rstrip()
            ss = line.split(" ")
            H, C = int(ss[0]), int(ss[1])
            HC.append((H,C))
        k += 1

    print getColoredIncreasingSeq(N, K, HC)
