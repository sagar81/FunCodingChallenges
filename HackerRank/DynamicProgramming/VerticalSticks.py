import sys
import math

def InitializeDicts(G, S, N, y):
    for i in range(N):
        s1, s2 = 0, 0
        G[y[i]], S[y[i]] = 0, 0
        for j in range(N):
            if i == j:
                continue
            if y[j] >= y[i]:
                s1 += 1
            else:
                s2 += 1
        G[y[i]] = s1
        S[y[i]] = s2
    return ;

def ExpectedSum(G, S, N, y):
    s = 0
    cache = {}
    
    for stick_height in y:
        nS, nG = S[stick_height], G[stick_height]
        for slot_index in range(N):
            numBeforeSlots = slot_index + 1
            for ray_length in range(1, numBeforeSlots+1):
                comb = 0
                if (nS, ray_length-1) in cache:
                        comb = cache[(nS, ray_length-1)]
                else:
                    comb = nCr(nS, ray_length-1, cache)
                    
                if ray_length == numBeforeSlots:  
                    # no stick higher or equal than stick_height
                    # select number of ways to get ray_length-1 smaller sticks from nS, 
                    # then permutate them. Permutate rest of the sticks right of stick in question.
                    # All these configurations will have ray length = ray_length
                    s +=  comb * math.factorial(ray_length-1) * math.factorial(N-ray_length) * ray_length
                else:
                    # select number of ways to get ray_length-1 smaller sticks from nS. 
                    # After that we need one longer or equal stick. Select number of ways to get one
                    # longer or equal stick from nG. Then find number of ways to put rest of the sticks
                    # in remaining slots. All these configurations will have ray length = ray_length
                    s += comb * math.factorial(ray_length-1) * nG * math.factorial(N-ray_length-1) * ray_length 
    return (1.0 * s) / math.factorial(N)                
    
def nCr(n, r, cache):
    if n < r:
        return 0.0
    elif r == 0 or r == n:
        return 1.0
    else:
        x = min(r, n-r)
        num, denom = 1.0, 1.0
        for i in range(1, x+1):
            num *= (n-i+1)
            denom *= i
        cache[(n, r)] = num / denom
        return num / denom
    
if __name__ == '__main__':
    k = 0
    N, M, num_cases = 0, 0, 0

    for line in sys.stdin:
        if  k == 0:
            num_cases = int(line.rstrip())
        else:
            line = line.rstrip()
            if k%2 == 1:
                N = int(line)
            else:
                ss = line.split(" ")
                y = map(int, ss)
                
                G, S  = {}, {}
                InitializeDicts(G, S, N, y)
                E = ExpectedSum(G, S, N, y)
                print("%.2f" % E)
        k += 1
