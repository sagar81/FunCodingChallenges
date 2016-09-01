# Enter your code here. Read input from STDIN. Print output to STDOUT

def UpdateCandiesEndToStart(candies, start, end):
    candies[end] = 1
    for i in range(end-1, start, -1):
        candies[i] = candies[i+1] + 1
    candies[start] = max(candies[start], (candies[start+1] + 1)) 

def UpdateCandiesStartToEnd(candies, start, end):
    candies[start] = 1
    for i in range(start+1, end+1):
        candies[i] = candies[i-1] + 1

def UpTurn(candies, ranks, start, end):
    if ranks[start] == ranks[end]:
        if start > 0:
            candies[(start+1):(end+1)] = [1]*(end-start)
        else:
            candies[start:(end+1)] = [1]*(end+1 - start)
    elif ranks[start] > ranks[end]:
        UpdateCandiesEndToStart(candies, start, end)
    else:
        print "Error", i, s1, s0, start, end, ranks[i-1], ranks[i], ranks[i+1]    

def DownTurn(candies, ranks, start, end):
    if ranks[start] == ranks[end]:
        if start > 0:
            candies[(start+1):(end+1)] = [1] * (end - start)
        else:
            candies[start:(end+1)] = [1] * (end+1 - start)
    elif ranks[start] < ranks[end]:
        UpdateCandiesStartToEnd(candies, start, end)
    else:
        print "Error", i, s1, s0, start, end, ranks[i-1], ranks[i], ranks[i+1]

def FlatTurn(candies, ranks, start, end):
    if ranks[start] < ranks[end]:
        UpdateCandiesStartToEnd(candies, start, end)
    elif ranks[start] > ranks[end]:
        UpdateCandiesEndToStart(candies, start, end)
    else: 
        print "Error", i, s1, s0, start, end, ranks[i-1], ranks[i], ranks[i+1]

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def OptimalCandies(ranks):
    s0 = ranks[1] - ranks[0]
    sz = len(ranks)
    start = 0
    #candies = np.zeros(sz)
    candies = [0] * sz
    for i in range(1,sz-1):
        s1 = ranks[i+1]-ranks[i]
        #print i, s0, s1, ranks[i], ranks[i+1]
        if sign(s1) != sign(s0):
            end = i
            if s1 > 0:
                UpTurn(candies, ranks, start, end)
            elif s1 < 0:
                DownTurn(candies, ranks, start, end)
            elif s1 == 0:
                FlatTurn(candies, ranks, start, end)
            start = end
        s0 = s1
 
    # last stretch
    if ranks[start] == ranks[sz-1]:
        candies[(start+1) : sz] = [1] * (sz - start - 1)
    elif ranks[start] > ranks[sz-1]:
        UpdateCandiesEndToStart(candies, start, sz-1)
    elif ranks[start] < ranks[sz-1]:
        UpdateCandiesStartToEnd(candies, start, sz-1)
 
    return candies

import sys

if __name__ == '__main__':
    k = 0
    ranks = []
    for line in sys.stdin:
        if  k == 0:
            num_children = int(line.rstrip())
        else:
            line = line.rstrip()
            ranks.append(int(line))
        k += 1
    candies = OptimalCandies(ranks)
    num_candies = 0
    for c in candies:
        num_candies += c
    print num_candies
