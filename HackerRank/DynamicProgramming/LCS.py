import sys

def InitializeTable(T, X, Y, n, m):
    t = [0] * m
    for i in range(n):
        T.append(list(t))
    
    for i in range(n):
        if Y[0] == X[i]:
            for k in range(i, n):
                T[k][0] = 1
            break
    
    for i in range(m):
        if X[0] == Y[i]:
            T[0][i:] = [1] * (m-i)
            break
    
    return T

def LCS_Length(T, X, Y, n, m):
    for i in range(1, n):
        for j in range(1, m):
            if X[i] == Y[j]:
                T[i][j] = T[i-1][j-1] + 1
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
    return T[n-1][m-1]

def LCS(T, X, Y, n, m):
    if n == -1 or m == -1:
        return " "
    if X[n] == Y[m]:
        return LCS(T, X, Y, n-1, m-1) + str(X[n]) + " "
    if n == 0 and T[n][m] == 1:
        return str(X[n]) + " "
    if m == 0 and T[n][m] == 1:
        return str(Y[m]) + " "
    elif T[n-1][m] >= T[n][m-1]:
        return LCS(T, X, Y, n-1, m)
    else:
        return LCS(T, X, Y, n, m-1)

if __name__ == '__main__':
    data = []
    for line in sys.stdin:
        line = line.rstrip()
        ss = line.split(" ")
        line = map(int, ss)
        data.append(line)
    n, m = data[0]
    X = data[1]
    Y = data[2]
    
    T = []
    T = InitializeTable(T, X, Y, n, m)
    l = LCS_Length(T, X, Y, n, m)
    print LCS(T, X, Y, n-1, m-1)
