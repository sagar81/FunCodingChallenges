import sys

def piecesCanFit(A):
    N = len(A[0])
    start_black_cell, end_black_cell = (-1, -1), (-1, -1)
    num_black_cells = 0
    for i in range(N):
        if A[0][i] == 0 and A[1][i] == 0:
            continue
        if A[0][i] == 1 and A[1][i] == 1:
            if num_black_cells % 2 == 1:
                return False
            else:
                start_black_cell, end_black_cell = (-1, -1), (-1, -1)
                continue             
        if A[0][i] == 1 and start_black_cell[0] < 0:
            num_black_cells += 1
            start_black_cell = (0, i)
        elif A[1][i] == 1 and start_black_cell[0] < 0:
            num_black_cells += 1
            start_black_cell = (1, i)
        elif A[0][i] == 1 and end_black_cell[0] < 0:
            num_black_cells += 1
            end_black_cell = (0, i)
            if start_black_cell[0] == 1 and (end_black_cell[1] - start_black_cell[1]) == 1:
                return False
            start_black_cell, end_black_cell = (-1, -1), (-1, -1)
        elif A[1][i] == 1 and end_black_cell[0] < 0:
            num_black_cells += 1
            end_black_cell = (1, i)
            start_black_cell, end_black_cell = (-1, -1), (-1, -1)
            
    if num_black_cells % 2 == 1:
        return False
    return True



if __name__ == '__main__':
    k = 0
    toprow, bottomrow = [], []

    for line in sys.stdin:
        if  k == 0:
            num_cases = int(line.rstrip())
        elif k % 3 == 1:
            N = int(line.rstrip())
        elif k % 3 == 2:
            line = line.rstrip()
            ss = line.split(" ")
            toprow = []
            for c in ss[0]:
                toprow.append(int(c))
        elif k % 3 == 0:
            line = line.rstrip()
            ss = line.split(" ")
            bottomrow = []
            for c in ss[0]:
                bottomrow.append(int(c))

            A = []
            A.append(toprow)
            A.append(bottomrow)

            if piecesCanFit(A):
                print 'YES'
            else:
                print 'NO'

        k += 1
