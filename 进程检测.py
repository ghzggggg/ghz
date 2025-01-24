for i in range(int(input())) :
    dic = {}
    mi = ma =0
    n = int(input())
    for j in range(n) :
        a,b = map(int,input().split())
        dic[j+1] = [a,b]
        mi = min(a,b,mi)
        ma = max(a,b,ma)
    L = []
    for x in range(mi,ma+1) :
        lx = []
        for m in range(n) :
            if x in range(dic[m+1][0],dic[m+1][1]+1) :
                lx.append(m)
        L.append(lx)
    def bi_ji(l) :
        return len(l)
    while True :
        cut = max((i for i in L), key=ni_ji)
        if cut == 0 : break