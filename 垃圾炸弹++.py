def lii_bo(ll) :
    l1 = list(sorted(ll, key=lambda x: x[0], reverse=True))
    l2 = list(sorted(ll, key=lambda x: x[1], reverse=True))
    q = sum(ll[m][2] for m in range(len(l)))
    return l1,l2,q
d = int(input())
l = [list(map(int,input().split())) for _ in range(int(input()))]
i = j = 0
while  :
    L1,L2,Q = lii_bo(l)
    if
