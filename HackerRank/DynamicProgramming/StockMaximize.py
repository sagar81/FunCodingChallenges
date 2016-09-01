# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def StockMaximize(stock):
    mx = stock[-1]
    sz = len(stock)
    profit = 0.
    for i in range(sz-2, -1, -1):
        if stock[i] < mx:
            # buy 1 at stock[i] which can be sold at mx
            profit += mx - stock[i]
        else:
            # reset mx
            mx = stock[i]
    return profit

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
                prices = map(int, ss)

                print int(StockMaximize(prices))
        k += 1
