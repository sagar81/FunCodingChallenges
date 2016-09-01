# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def FightingStrategy(sorted_health):
    P0 = sum(sorted_health)
    P = P0
    N = len(sorted_health)
    MaxSum = P
    S = 1
    removed_set = 0
    for i in range(N):
        removed_set += sorted_health[i]
        P = (P - S*sorted_health[i]) + (P0 - removed_set)
        if P < MaxSum:
            break
        else:
            MaxSum = P
            S = S+1
    return MaxSum        
        
if __name__ == '__main__':
    k = 0
    N, num_cases = 0, 0
    MapNumPaths = {}

    for line in sys.stdin:
        if  k == 0:
            num_cases = int(line.rstrip())
        else:
            line = line.rstrip()
            ss = line.split(" ")
            if k%2 == 1:
                N = int(ss[0])
            else:
                D = map(int, ss)
                print FightingStrategy(sorted(D))
        k += 1
