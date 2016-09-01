# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def BuildEdges(row, col, G, n, m, M):
    start_row, start_col = max(0, row-1), max(0, col-1)
    end_row, end_col = min(n-1, row+1), min(m-1, col+1)
    for i in range(start_row, end_row+1):
        for j in range(start_col, end_col+1):
            #if (i == row and j == col) == False:
            if M[i][j] == 1:
                if (row,col) in G:
                    G[(row,col)].add((i, j))
                else:
                    G[(row,col)] = set([(i,j)])

def ConstructGraph(rows, cols, M):
    G = {}
    for i in range(rows):
        for j in range(cols):
            if M[i][j] == 1:
                BuildEdges(i, j, G, rows, cols, M)
    
    return G

if __name__ == '__main__': 
    k = 0
    rows, cols = 0, 0
    mat = []

    for line in sys.stdin:
        if  k == 0:
            rows = int(line.rstrip())
        elif  k == 1:
            cols = int(line.rstrip())
        else:
            line = line.rstrip()
            ss = line.split(" ")
            mat.append(map(int, ss))
        k += 1

    G = ConstructGraph(rows, cols, mat)
    UsedKeys = {}
    max_region_size = 0
    for key in G:
        if key in UsedKeys:
            continue
        region = bfs(G, key)
        for node in region:
            UsedKeys[node] = 1
        
        if len(region) > max_region_size:
            max_region_size = len(region)
    print max_region_size   
