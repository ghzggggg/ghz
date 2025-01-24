for _ in range(int(input())):
    n = int(input())
    ln = list(map(int,input().split()))
    l = []
    for i in range(0,2*n,2):
        l.append((ln[i],ln[i+1]))
    l.sort()
    a=0
    while l:
        lo = [l[0]]
        for i in range(1,len(l)):
            if l[i][1]>=lo[-1][1]:
                lo.append(l[i])
        for i in lo :
            l.remove(i)
        a+=1
    print(a)