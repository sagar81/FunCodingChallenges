# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

# Definitions
# Cn : number of nodes after nth step
# Sn : sum of distances between each pair after nth step
# Rn : Sum of distances from one of the root nodes to the rest of the nodes after nth step
# dn : longest path length in the graph after nth step

def SumOfDistances(N, A):
    r = 1000000007
    # Initialization
    C, S, R, d = 1, 0, 0, 0
    for i in range(N):
        X = (2*C*R + C*C*2*A[i]) % r
        Y = (2*C*R + C*C*3*A[i]) % r
        Z = (8*R + (12*C+1)*A[i])%r
        S = (4*S + 2*X + 4*Y + Z)%r

        # update variables
        R = (4*R + 8*C*A[i] + 3*d*C + 3*A[i] + 2*d) % r
        d = (2*d + 3*A[i]) % r
        C = (4*C+2) % r

    return S%1000000007
    
if __name__ == '__main__':
    k = 0
    N = 0

    for line in sys.stdin:
        if  k == 0:
            N = int(line.rstrip())
        else:
            line = line.rstrip()
            ss = line.split(" ")
            A = map(int, ss)
            print SumOfDistances(N, A)
        k += 1

