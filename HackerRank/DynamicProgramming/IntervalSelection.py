from operator import itemgetter

# Solution requires to identify that once we sort the list of tuples on first element then 
# only the last two entries in this list is important whose second element of tuple needs to be compared
# with the new entry and one of the entries to be updated if required.

def Intervals(N, I, S):
    if I[0][1] == I[1][1]:
        S = {I[0][1] : [I[0], I[1]]}
    else:
        S = {I[0][1] : [I[0]], I[1][1] : [I[1]]}
    bMax, bSecondMax = max(I[0][1], I[1][1]), min(I[0][1], I[1][1])

    for i in range(2, len(I)):
        aNew = I[i][0]
        bNew = I[i][1]
        if aNew > bSecondMax:
            if bNew in S:
                S[bNew].append(I[i])
            else:
                S[bNew] = [I[i]]
            if bMax > bNew:
                bSecondMax = bNew
            else:
                bSecondMax = bMax
                bMax = bNew
        else:
            if bNew in S:
                S[bNew].append(I[i])
            else:
                S[bNew] = [I[i]]
            keyToRemove = max(bNew, bMax)
            x = sorted([bSecondMax, bMax, bNew])
            bSecondMax, bMax = x[0], x[1]
            if len(S[keyToRemove]) == 1:
                del S[keyToRemove]
            else:
                del S[keyToRemove][0]
    
    result = 0
    for key in S:
        result += len(S[key])
    return result    

if __name__ == '__main__':
    test = int(raw_input())
    for t in range(0, test):
        N = int(raw_input())
        I = []
        S = {}

        for i in range(0, N):
            numbers = raw_input()
            a, b = [int(x) for x in numbers.split(' ')]
            I.append((a, b))

        I = sorted(I,key=itemgetter(0))
        result = Intervals(N, I, S)
        print result

