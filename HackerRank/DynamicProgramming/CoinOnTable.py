INF = 1000000
import sys

def InitializeSoln(rows, cols):
    OpsDict = {}
    for i in range(rows):
        for j in range(cols):
            OpsDict[(i, j, 0)] = INF
    OpsDict[(0, 0, 0)] = 0
    return OpsDict

def Operations(A, rows, cols, K, starred_row, starred_col):
    for k in range(1, K+1):
        for i in range(rows):
            for j in range(cols):
                operations = []
                if i-1 >= 0 and (i-1, j) != (starred_row, starred_col):
                    move = NumberOfOperations(A, i-1, j, i, j, starred_row, starred_col)
                    move += OpsDict[(i-1, j, k-1)]
                    operations.append(move)
                if i+1 < rows and (i+1, j) != (starred_row, starred_col):
                    move = NumberOfOperations(A, i+1, j, i, j, starred_row, starred_col)
                    move += OpsDict[(i+1, j, k-1)]
                    operations.append(move)
                if j-1 >= 0 and (i, j-1) != (starred_row, starred_col):
                    move = NumberOfOperations(A, i, j-1, i, j, starred_row, starred_col)
                    move += OpsDict[(i, j-1, k-1)]
                    operations.append(move)
                if j+1 < cols and (i, j+1) != (starred_row, starred_col):
                    move = NumberOfOperations(A, i, j+1, i, j, starred_row, starred_col)
                    move += OpsDict[(i, j+1, k-1)]
                    operations.append(move)
                ops = min(operations)
                OpsDict[(i, j, k)] = ops
    return OpsDict 

def MinOps(OpsDict):
    minOps = INF
    for k in range(K+1):
        if minOps > OpsDict[(starred_row, starred_col, k)]:
            minOps = OpsDict[(starred_row, starred_col, k)]
    if minOps == INF:
        return -1
    return minOps

def NumberOfOperations(A, i, j, target_row, target_col, starred_row, starred_col):
    if target_row-1 == i and target_col == j and A[i][j] != 'D':
        return 1
    elif target_row+1 == i and target_col == j and A[i][j] != 'U':
        return 1
    elif target_row == i and target_col-1 == j and A[i][j] != 'R':
        return 1
    elif target_row == i and target_col+1 == j and A[i][j] != 'L':
        return 1
    return 0

import sys

if __name__ == '__main__':
    A = []
    k, iteration , starred_row, starred_col = 0, 0, 0, 0

    for line in sys.stdin:
        if  k == 0:
            line = line.rstrip()
            ss = line.split(" ")
            N, M, K = int(ss[0]), int(ss[1]), int(ss[2])
        else:
            line = line.rstrip()
            row = []
            col = 0
            for c in line:
                row.append(c)
                if c == '*':
                    starred_row, starred_col = iteration, col
                col += 1
            A.append(row) 
            iteration += 1
        k += 1

    OpsDict = InitializeSoln(N, M)
    OpsDict = Operations(A, N, M, K, starred_row, starred_col)
    print MinOps(OpsDict)
