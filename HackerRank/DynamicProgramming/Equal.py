import sys

def getMinOperations_1(C, N):
    operations, S = 0, 0
    for i in range(1, N):
        operations += getOpsForOneChange_1(C[0]+S, C[i]+S)
        S += (C[i]-C[0])
    return operations

def getOpsForOneChange_1(a, b):
    x1, y1 = (b-a) / 5, (b-a) % 5
    x2, y2 = y1 / 2, y1 % 2
    x3 = y2
    return x1+x2+x3

def getMinOperations(C, N):
    operations, S = 0, 0
    S1, S2 = 0, 0
    for i in range(1, N):
        if i == 1:
            opt = getOpsForOneChange(C[0]+S, C[i]+S, i)
            operations += opt[0]
            S1 = (C[i]-C[0])
            S2 = opt[2] + opt[3]
            secondIncr = opt[3]
        if i == 2:
            opt1 = getOpsForOneChange(C[0]+S1, C[i]+S1, i)
            opt2 = getOpsForOneChange(C[0]+S2-secondIncr, C[i]+S2, i)
            if opt1[0] < opt2[0]:
                S = S1
                operations += opt1[0]
                secondIncrSelected = False
            else:
                S = S2
                operations += opt2[0]
                secondIncrSelected = True
            S += (C[i]-C[0])
        elif i > 2:
            if secondIncrSelected:
                opt = getOpsForOneChange(C[0]+S-secondIncr, C[i]+S, i)
            else:
                opt = getOpsForOneChange(C[0]+S, C[i]+S, i)
            operations += opt[0]
            S += (C[i]-C[0]) 
    return operations

def getOpsForOneChange(a, b, iteration):
    x1, y1 = (b-a) / 5, (b-a) % 5
    x2, y2 = y1 / 2, y1 % 2
    x3 = y2
    firstSoln = x1+x2+x3
    
    secondSoln, increment1, increment2 = 0, 0, 0
    if iteration == 1:
        if y1 > 0 and y1 == 3:
            secondSoln = x1 + 2
            increment1, increment2 = 5, 2  # first give 5 to a and then 2 to b
        elif y1 > 0 and y1 == 4:
            secondSoln = x1 + 2
            increment1, increment2 = 5, 1 # first give 5 to a and then 1 to b
    
    return [firstSoln, secondSoln, increment1, increment2]

if __name__ == '__main__':
    k = 0
    N, num_cases = 0, 0

    for line in sys.stdin:
        if  k == 0:
            num_cases = int(line.rstrip())
        else:
            line = line.rstrip()
            if k%2 == 1:
                N = int(line)
            else:
                ss = line.split(" ")
                C = map(int, ss)
                print min(getMinOperations_1(sorted(C), N), getMinOperations(sorted(C), N))
        k += 1
