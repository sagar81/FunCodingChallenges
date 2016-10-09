def FindMaxSum(B):
    optS = (0, 0)
    for i in range(1, len(B)):
        s1 = WhenAiEquals1(optS, B[i-1])
        s2 = WhenAiEqualsBi(optS, B[i], B[i-1])
        optS = (s1, s2)
    return max(optS[0], optS[1])

def WhenAiEquals1(optS, prevB):
    s1 = optS[0] + abs(1-1)
    s2 = optS[1] + abs(1-prevB)
    return max(s1, s2)

def WhenAiEqualsBi(optS, currB, prevB):
    s1 = optS[0] + (currB - 1) 
    s2 = optS[1] + (currB - prevB)
    return max(s1, s2)

import sys

k = 0
N, M, num_cases = 0, 0, 0

for line in sys.stdin:
    if  k == 0:
        num_cases = int(line.rstrip())
    else:
        line = line.rstrip()
        if k%2 == 1:
            N = int(line[0])
        else:
            ss = line.split(" ")
            B = map(int, ss)
            print FindMaxSum(B)
    k += 1
