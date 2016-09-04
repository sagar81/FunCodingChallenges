import sys
sys.setrecursionlimit(100001)

# I can't find the error in following logic.
# But code times out for large nodes in python but works in C, C++.
# Logic assigns the sum of weights of nodes of the subtree to the root of that subtree including its weight. This is done by running a sightly modified dfs.

def ConstructGraph(edges):
    G = {}
    for e in edges:
        u, v = e[0], e[1]
        if u in G:
            G[u].append(v)
        else:
            G[u] = [v]
        if v in G:
            G[v].append(u)
        else:
            G[v] = [u]
    return G

def dfs_modified(G, start, N, W, S, visited):
    visited.append(start)
    neighbors = G[start]
    retVal = 0
    for neigh in neighbors:
        if neigh not in visited:
            retVal += dfs_modified(G, neigh, N, W, S, visited)
    
    S[start-1] = W[start-1] + retVal
    return S[start-1]

def MinCutTree(G, N, W, S, edges):
    total = sum(W)
    minDiff = sys.maxint
    for e in edges:
        u, v = e[0], e[1]
        x = min(S[u-1], S[v-1])
        diff = abs((total - x) - x)
        if diff < minDiff:
            minDiff = diff
    return minDiff

if __name__ == '__main__':
    k = 0
    edges = []
    for line in sys.stdin:
        if  k == 0:
            N = int(line.rstrip())
            print N
        elif k == 1:
            line = line.rstrip()
            ss = line.split(" ")
            W = map(int, ss)
            print W
        else:
            line = line.rstrip()
            ss = line.split(" ")
            edges.append((int(ss[0]), int(ss[1])))
        k += 1

    G = ConstructGraph(edges)
    visited = []
    dfs_modified(G, 1, N, W, S, visited)
    print MinCutTree(G, N, W, S, edges)
