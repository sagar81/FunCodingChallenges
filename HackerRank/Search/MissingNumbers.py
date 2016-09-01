import sys

def FindMissingNumbers(A, B):
    dA, dB = {}, {}
    for a in A:
        if a in dA:
            dA[a] += 1
        else:
            dA[a] = 1
            
    for b in B:
        if b in dB:
            dB[b] += 1
        else:
            dB[b] = 1
    
    output = []
    for b in dB:
        if b in dA:
            if dB[b] - dA[b] > 0:
                output.append(b)
        else:
            output.append(b)
    
    output = sorted(output)
    return output

if __name__ == '__main__':
    k = 0

    for line in sys.stdin:
        if  k == 0:
            n = int(line.rstrip())
        if k == 1:
            line = line.rstrip()
            ss = line.split(" ")
            A = map(int, ss)
        if  k == 2:
            m = int(line.rstrip())
        if k == 3:
            line = line.rstrip()
            ss = line.split(" ")
            B = map(int, ss)

            result = FindMissingNumbers(A, B)
            print " ".join(map(str, result))

        k += 1
