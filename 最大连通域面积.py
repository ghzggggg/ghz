def max_ever(l,n1,m1):
    delta = [(1,1),(-1,1),(1,-1),(-1,-1),(0,1),(1,0),(-1,0),(0,-1)]
    stack = []
    max_even = 0
    for i in range(1,n1+1):
        for j in range(1,m1+1):
            q = 0
            if l[i][j] == 'W':
                stack.append((i,j))
                l[i][j] = '.'
                q +=1
            while stack:
                x,y = stack.pop()
                for dx,dy in delta:
                    if l[x+dx][y+dy] == 'W':
                        stack.append((x+dx,y+dy))
                        l[x+dx][y+dy] = '.'
                        q+=1
            max_even = max(max_even,q)
    return max_even

for _ in range(int(input())):
    n,m = map(int,input().split())
    ll = [['.']*(m+2)]
    for _ in range(n):
        li = ['.']+list(input())+['.']
        ll.append(li)
    ll.append(['.']*(m+2))
    print(max_ever(ll,n,m))