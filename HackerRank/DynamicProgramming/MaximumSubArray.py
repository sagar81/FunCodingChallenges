# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def MaxSumSubArray(N, a):
    Sum, MaxContiguosSum, MaxNonContiguosSum, MaxEntry = 0, -sys.maxint, 0, -sys.maxint
    
    for i in range(N):
        Sum += a[i]
        if Sum > MaxContiguosSum:
            MaxContiguosSum = Sum
        elif Sum < 0:
            Sum = 0
        
        if a[i] > 0:
            MaxNonContiguosSum += a[i]
        elif a[i] > MaxEntry and MaxNonContiguosSum <= 0:
            MaxEntry = a[i]
    
    if MaxNonContiguosSum == 0:
        MaxNonContiguosSum = MaxEntry
        MaxContiguosSum = MaxEntry
    
    return [MaxContiguosSum, MaxNonContiguosSum]

if __name__ == '__main__':
    k = 0
    N = 0

    for line in sys.stdin:
        if  k == 0:
            num_cases = int(line.rstrip())
        else:
            line = line.rstrip()
            ss = line.split(" ")
            if k%2 == 1:
                N = int(ss[0])
            else:
                a = map(int, ss)
                result = MaxSumSubArray(N, a)
                print result[0], result[1]
        k += 1
