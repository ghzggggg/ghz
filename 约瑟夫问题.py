while True :
    mn = str.split(input())
    m = int(mn[1])
    n = int(mn[0])
    if m == 0 :
        break
    l = list(range(1,n+1))
    k = int(mn[1])
    while len(l) > 1 :
        del l[k%len(l)- 1]
        if k%(len(l)+1) == 0 :
            k = k%(len(l)+1)+m
        else :
            k = k%(len(l)+1)+m-1
    print(l[0])