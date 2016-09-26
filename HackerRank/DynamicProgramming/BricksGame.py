# Build the solution from back.
# Best solution is the maximum of the following three potential solutions at each step.
# a. When you only pick first brick and let the opponent make his move after that.
# b. When you only pick first and second brick and let the opponent make his move after that.
# c. When you pick first, second and third brick and let the opponent make his move after that.


def MaxSum(a, N):
    if N <= 3:
        s = 0
        for e in a:
            s += e   
        return s
    
    reverseCumsum, optSoln = [0] * N, [0] * N
    s = 0
    for i in range(N-1, -1, -1):
        s += a[i]
        reverseCumsum[i] = s
        if i >= N-3:
            optSoln[i] = s
        else:
            s1 = a[i] + reverseCumsum[i+1] - optSoln[i+1]
            s2 = a[i] + a[i+1] + reverseCumsum[i+2] - optSoln[i+2]
            s3 = a[i] + a[i+1] + a[i+2] + reverseCumsum[i+3] - optSoln[i+3]
            optSoln[i] = max(s1, max(s2, s3))
    
    return optSoln[0]        

if __name__ == '__main__':
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
                a = map(int, ss)
                print MaxSum(a, N)
        k += 1
