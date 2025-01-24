def cherish_map(l,m1,n1):
    di = {}
    for i in range(1,m1+1):
        for j in range(1,n1+1):
            if l[i][j] == 0:
                di[(i,j)] = m1*n1
    stack,di[(1,1)] = [(1,1,0)],0
    delta = [(-1,0),(0,1),(1,0),(0,-1)]
    ans = m1*n1
    if l[1][1] == 1:
        return 0
    while stack:
        x,y,s = stack.pop()
        if s>=ans:pass
        else:
            for dx, dy in delta:
                if l[x + dx][y + dy] == 0 and di[(x+dx,y+dy)] > s+1:
                    di[(x+dx,y+dy)] = s+1
                    stack.append((x + dx, y + dy, s + 1))
                if l[x + dx][y + dy] == 1:
                    ans = min(ans, s + 1)

    if ans != m1*n1:  return ans
    else:             return 'NO'

m,n = map(int,input().split())
ll = [[2]*(n+2)]
for _ in range(m):
    li = [2]+list(map(int,input().split()))+[2]
    ll.append(li)
ll.append([2]*(n+2))
print(cherish_map(ll,m,n))