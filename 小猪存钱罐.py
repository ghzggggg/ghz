import math
for _ in range(int(input())):
    e,f = map(int,input().split())
    m = f-e
    n = int(input())
    l = []
    for _ in range(n):
        a,b = map(int,input().split())
        if b <= m :
            l.append((a,b))
    q = [0]+[math.inf]*m
    for j in range(len(l)):
        w,t = l[j][1],l[j][0]
        for i in range(w,m+1):
            if q[i-w] != math.inf :
                q[i] = min(q[i],q[i-w]+t)
    if q[-1] == math.inf :
        print('This is impossible.')
    else:
        print('The minimum amount of money in the piggy-bank is '+str(q[-1])+'.')