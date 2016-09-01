# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

# Initialization of storage table
def Initialization(N, M):
    row = [0] * (N+1)
    storage = [row for i in range(M)]

    # If N = 0 there is only one way to construct by not selecting any of the coins
    for i in range(M):
        storage[i][0] = 1
    return storage
    

def GetConfigurations(N, M, C, storage):
    for i in range(M):
        for j in range(1, N+1):
            first_term, second_term = 0, 0
            if j-1 >= 0:
                first_term = storage[i-1][j]
            if j-C[i] >= 0:
                second_term = storage[i][j-C[i]]
            storage[i][j] = first_term + second_term

    return storage[M-1][N]

if __name__ == '__main__':
    k = 0
    N, M = 0, 0

    for line in sys.stdin:
        line = line.rstrip()
        ss = line.split(" ")
        if  k == 0:
            N, M = int(ss[0]), int(ss[1])
        else:
            D = map(int, ss)
            table = Initialization(N, M)
            print GetConfigurations(N, M, D, table)
        k += 1
