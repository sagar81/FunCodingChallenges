
import sys

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def ConstructGraph(rows, cols, A):
    G = {}
    for i in range(rows):
        for j in range(cols):
            if A[i][j] == '.' or A[i][j] == 'M' or A[i][j] == '*':
                G[(i, j)] = set([(i,j)])
                node_1 = (i, max(0, j-1))
                node_2 = (i, min(cols-1, j+1))
                node_3 = (max(0, i-1), j)
                node_4 = (min(rows-1, i+1), j)
                if A[node_1[0]][node_1[1]] == '.' or A[node_1[0]][node_1[1]] == 'M' or A[node_1[0]][node_1[1]] == '*':
                    G[(i, j)].add(node_1)
                
                if A[node_2[0]][node_2[1]] == '.' or A[node_2[0]][node_2[1]] == 'M' or A[node_2[0]][node_2[1]] == '*':
                    G[(i, j)].add(node_2)
                
                if A[node_3[0]][node_3[1]] == '.' or A[node_3[0]][node_3[1]] == 'M' or A[node_3[0]][node_3[1]] == '*':
                    G[(i, j)].add(node_3)
                
                if A[node_4[0]][node_4[1]] == '.' or A[node_4[0]][node_4[1]] == 'M' or A[node_4[0]][node_4[1]] == '*':
                    G[(i, j)].add(node_4)
    
    return G

def NumOfTimesWandUsed(path, G):
    l = len(path)
    wand_used = 0
    prev_node = None
    for i in range(l-1):
        if len(G[path[i]]) == 3 and prev_node not in G[path[i]]:
            wand_used += 1
        elif len(G[path[i]]) > 3:
            wand_used += 1
        prev_node = path[i]    
    return wand_used


if __name__ == '__main__':
    k = 0
    rows, cols, iteration, K = 0, 0, 0, 0

    for line in sys.stdin:
        if  k == 0:
            num_cases = int(line.rstrip())
        else:
            line = line.rstrip()
            ss = line.split(" ")
            if len(ss) == 2:
                ss = map(int, ss)
                n, m = int(ss[0]), int(ss[1])
                iteration, start_pos, portkey_pos = 0, (-1,-1), (-1,-1)
                forest = []
            elif ss[0][0] == 'X' or ss[0][0] == '.' or ss[0][0] == '*' or ss[0][0] == 'M':
                forest.append(list(ss[0]))
                for i in range(m):
                    if ss[0][i] == 'M':
                        start_pos = (iteration, i)
                    if ss[0][i] == '*':
                        portkey_pos = (iteration, i)
                iteration += 1
            else:
                K = int(ss[0])
                G = ConstructGraph(n, m, forest)
                path = shortest_path(G, start_pos, portkey_pos)
                if NumOfTimesWandUsed(path, G) == K:
                    print 'Impressed'
                else:
                    print 'Oops!'
                
                
        k += 1

