# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math

def Factorial(n, FactorialDict):
    if n in FactorialDict:
        return FactorialDict[n]
    else:
        key = max(k for k in FactorialDict if k <= n)
        value = FactorialDict[key]
        for i in range(key+1, n+1):
            value = value * i
        FactorialDict[n] = value
        return value

def GetNumConfigurations(N, Fours, Ones, FactorialDict):
    configurations = 0
    while Fours >= 0:
        configurations += Factorial(Ones+Fours, FactorialDict) / ( Factorial(Ones, FactorialDict) * Factorial(Fours, FactorialDict) )
        Fours = Fours - 1
        Ones = Ones + 4
    return configurations

def GetPrimes(configurations):
    PrimesList = [2]
    if configurations == 1:
        return 0
    if configurations == 2:
        return 1
    for i in range(3, configurations+1):
        sqroot = math.sqrt(i)
        isPrime = True
        for prime in PrimesList:
            if prime <= sqroot and i%prime == 0:
                isPrime = False
                break
            elif prime > sqroot:
                break
                
        if isPrime:
            PrimesList.append(i)
    return len(PrimesList)

if __name__ == '__main__':
    k = 0
for line in sys.stdin:
    if  k == 0:
        num_cases = int(line.rstrip())
    else:
        line = line.rstrip()
        N = int(line)
        Fours = int(N/4)
        Ones = N - 4*Fours
        FactorialDict = {}
        FactorialDict[0] = 1
        M = GetNumConfigurations(N, Fours, Ones, FactorialDict)
        print GetPrimes(M)
    k += 1
