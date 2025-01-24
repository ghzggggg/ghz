n,m = map(int,input().split())
a_map = [list(map(int,input().split())) for _ in range(n)]
q_map = [list(map(int,input().split())) for _ in range(n)]
stack = [([(0,0)],q_map[0][0])]
dr = [(0,1),(1,0),(-1,0),(0,-1)]
ans = -float('inf')

while stack:
    l,q = stack.pop()
    x,y = l[-1]
    if x==n-1 and y==m-1:
        ans = max(ans,q)
    for dx,dy in dr :
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not a_map[nx][ny] and (nx,ny) not in l :
            l1 = l[:]
            l1.append((nx,ny))
            stack.append((l1,q+q_map[nx][ny]))

print(ans)