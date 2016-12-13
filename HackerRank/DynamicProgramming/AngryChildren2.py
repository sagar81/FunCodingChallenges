
# 1. Make sure you understand the logic why sorting helps. We can only have solution
# with consecutive incresing/decreasing numbers. It can be proved with simple examples and reasoning.
# 2. Rest is understanding the pattern of calculating unfariness so that we can update it in a linear time.

def MinimumUnfairness(N, K, X):
    S, unfairness = 0, 0
    for i in range(K):
        S += X[i]
        unfairness += (X[i] * (2*i - K + 1))  #  i*X[i] - (K-1-i) * X[i]

    minUnfairness = unfairness    
    for i in range(K, N):
        S = S + X[i] - X[i-K]
        unfairness += ( (K-1) * (X[i] + X[i-K]) - 2 * (S-X[i]) )
        if unfairness < minUnfairness:
            minUnfairness = unfairness
            
    return minUnfairness

if __name__ == '__main__':
    N = int(raw_input())
    K = int(raw_input())
    candies = []
    for i in xrange(0, N):
        candies.append(int(raw_input()))
    candies.sort()
    print MinimumUnfairness(N, K, candies)
