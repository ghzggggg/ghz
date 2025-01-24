s = input()
p = input()
n,m = len(s),len(p)
lp,ls,ans = list(p),list(s),[]
if m > n:
    print(ans)
else:
    l, l1 = ls[:m], []
    for i in lp:
        if i in l:
            l.remove(i)
        else:
            l1.append(i)

    for pos in range(0, n - m):
        if not l: ans.append(pos)
        if l and l[0] == ls[pos]:
            del l[0]
        else:
            l1.append(ls[pos])
        if ls[pos + m] in l1:
            l1.remove(ls[pos + m])
        else:
            l.append(ls[pos + m])
        print(l,l1)
    if not l: ans.append(n - m)
    print(ans)