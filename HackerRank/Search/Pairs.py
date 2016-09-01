import sys
import bisect

def index(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

def GetPairs(N, K, A):
    A = sorted(A)
    l = len(A)
    pairs = 0
    for i in range(l):
        look_for = A[i] + K
        if look_for > A[-1]:
            break
        if index(A, look_for) is not None:
            pairs += 1
    return pairs        

if __name__ == '__main__':

    k = 0
    N, K = 0, 0

    for line in sys.stdin:
        ss = line.rstrip()
        ss = line.split(" ")
        if  k == 0:
            N, K = int(ss[0]), int(ss[1])
        else :
            A = map(int, ss)
            print GetPairs(N, K, A)
        k += 1
