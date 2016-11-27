# This problem is equilvalent to knapsack problem.
# There exists a solution if half of sum(A) can be arranged
# in G capacity. The rest can be arranged because two tasks at a
# time is allowed. Equivalent to optimal scheduling of tasks
# to minimize final completion time on two processors.
# We use DP for knapsack in DoesArrangementExist(N, G, A).

import sys
import math

def DoesArrangementExist(N, G, A):
    S = sum(A)
    S = math.ceil(S/2)
    
    row = [0] * (N)
    T = [list(row) for i in range(G+1)]
    
    for i in range(G+1):
        if i >= A[0]:
            T[i][0] = A[0]
    
    for i in range(1, G+1):
        for j in range(1, N):
            if A[j] > i:
                T[i][j:] = [T[i][j-1] for k in range(len(A) - j)] 
                continue 
            y = 0
            if i - A[j] >= 0:
                y = T[i-A[j]][j-1]
                
            T[i][j] = max(T[i][j-1], y+A[j])
            
            if T[i][j] >= S:
                return 'YES'
            
    if T[G][N-1] >= S:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    k = 0
    N, G, num_cases = 0, 0, 0

    for line in sys.stdin:
        if  k == 0:
            num_cases = int(line.rstrip())
        else:
            line = line.rstrip()
            ss = line.split(" ")
            if k%2 == 1:
                N, G = int(ss[0]), int(ss[1])
            else:
                A = map(int, ss)
                print DoesArrangementExist(N, G, A)
        k += 1
