import sys

def NthFibonacci(t1, t2, n):
    ti_1, ti_2 = t2, t1
    for i in range(3, n+1):
        ti = ti_1*ti_1 + ti_2
        ti_2 = ti_1
        ti_1 = ti
    
    return ti

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.rstrip()
        ss = line.split(" ")
        t1, t2, n = int(ss[0]), int(ss[1]), int(ss[2])
        print NthFibonacci(t1, t2, n)
